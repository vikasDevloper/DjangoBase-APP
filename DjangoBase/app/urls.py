from app.product import ProductView
from django.urls import path
from django.urls.conf import include

urlpatterns = [path("products", ProductView.as_view(), name="run.migrations")]
