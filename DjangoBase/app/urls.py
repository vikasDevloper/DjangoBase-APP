from app.product import LongestWord, ProductView, SearchRecords
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("products", ProductView.as_view(), name="run.migrations"),
    path("wordfinder", LongestWord.as_view(), name="run.migrations"),
    path("search/record", SearchRecords.as_view(), name="run.migrations"),
]
