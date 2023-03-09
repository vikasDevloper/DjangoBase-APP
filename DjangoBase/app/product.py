from app.models import Product, ProductViewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def api_response(code, message, data, status=None):
    if status is not None and status == 0:
        data = {
            "status": status if status is not None else code,
            "message": message,
            "error": data,
        }
    else:
        data = {
            "status": status if status is not None else code,
            "message": message,
            "data": data,
        }
    return Response(data=data, status=code)


class ProductView(APIView):
    def get(self, request):
        # data = {"name": "vikas"}
        da = Product.objects.filter()
        data = ProductViewSerializer(da, many=True)
        return api_response(status.HTTP_200_OK, "Successfully Fetched data", data.data, 1)

    def post(self, request):
        data = request.data
        registered_event_serializer = ProductViewSerializer(data=data)
        registered_event_serializer.is_valid(raise_exception=True)
        registered_event_serializer.save()
        return api_response(status.HTTP_200_OK, "row inserted", data, 1)
