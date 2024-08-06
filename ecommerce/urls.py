"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/auth/profile/', views.ProfileView.as_view(), name='profile'),
    path('api/products/', views.ProductListView.as_view(), name='product-list'),
    path('api/products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/cart/', views.CartView.as_view(), name='cart'),
    path('api/cart/add/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/update/', views.UpdateCartItemView.as_view(), name='update-cart-item'),
    path('api/cart/remove/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('api/cart/remove/<int:product_id>/', views.CartItemDeleteView.as_view(), name='cart-item-remove'),
    path('api/orders/', views.OrderListView.as_view(), name='order-list'),
    path('api/orders/<int:id>/', views.OrderDetailView.as_view(), name='order-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



