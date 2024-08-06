class PrintHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("Request Headers:", request.headers)
        print("Response Headers:", response.headers)
        return response