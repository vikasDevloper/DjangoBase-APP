import json

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

    def put(self, request):
        f = open("/Users/abhishekgoswami/vikas/DjangoBase-APP/DjangoBase/app/product.json")
        # with open("/Users/abhishekgoswami/vikas/DjangoBase-APP/DjangoBase/app/product.json", "r") as f:
        print("hksjfk")
        print(f)
        #     data = json.load(f)
        data = json.loads(f.read())
        for d in data["products"]:
            registered_event_serializer = ProductViewSerializer(data=d)
            registered_event_serializer.is_valid(raise_exception=True)
            registered_event_serializer.save()
        f.close()
        return api_response(status.HTTP_200_OK, "row inserted", data, 1)


class LongestWord(APIView):
    def get(self, request):
        s_word = request.query_params.get("word")
        word_json = ["sales", "look", "english", "leftabhish", "team", "estate", "box", "conditions"]
        map = {}
        for w in word_json:
            char_array = list(s_word)
            count = 0
            c_array = list(w)
            for c in c_array:
                if c in char_array:
                    char_array.remove(c)
                    count = count + 1
            map[w] = count
        max = 0
        for m in map:
            if max < map[m]:
                max = map[m]
                val = m
        return api_response(status.HTTP_200_OK, "data", val, 1)


class SearchRecords(APIView):
    def get(self, request):
        s_word = request.query_params.get("product")
        da = Product.objects.filter()
        data = ProductViewSerializer(da, many=True)
        map = {}
        for w in data.data:
            print(w["name"])
            char_array = list(s_word)
            count = 0
            c_array = list(w["name"])
            for c in c_array:
                if c in char_array:
                    char_array.remove(c)
                    count = count + 1
            map[w["name"]] = count
        max = 0
        for m in map:
            if max < map[m]:
                max = map[m]
                val = m
        return api_response(status.HTTP_200_OK, "data", val, 1)
