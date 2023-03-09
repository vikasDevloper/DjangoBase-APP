from django.urls import path
from django.urls.conf import include

from app.product import ProductView

urlpatterns = [
    path("products", ProductView.as_view(), name="run.migrations"),
]