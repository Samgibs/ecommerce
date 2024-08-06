from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'user_type']

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'seller']
        read_only_fields = ['seller']

    def create(self, validated_data):
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)

class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = CartItem.objects.get(id=item_id, cart=instance)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                CartItem.objects.create(cart=instance, **item_data)
        
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context.get('request')
        for item in response['items']:
            item['product']['image'] = request.build_absolute_uri(item['product']['image'])
        return response

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'status', 'created_at']
        read_only_fields = ['user', 'total_price', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(user=self.context['request'].user, total_price=0, **validated_data)

        total_price = 0
        for item_data in items_data:
            product_id = item_data.pop('product_id')
            product = Product.objects.get(id=product_id)
            cart_item = CartItem.objects.create(product=product, **item_data)
            order.items.add(cart_item)
            total_price += product.price * item_data['quantity']
        
        order.total_price = total_price
        order.save()
        
        return order


