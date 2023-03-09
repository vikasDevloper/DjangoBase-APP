from django.contrib import admin
from django.db import models
from rest_framework import serializers

# Create your models here.


class Product(models.Model):
    # lookup_types = (("work", "work"), ("okr", "okr"), ("script", "script"), ("web_service", "web_service"))
    name = models.CharField(max_length=191, null=True, blank=True, unique=True)
    reference = models.AutoField(primary_key=True)
    volume = models.CharField(max_length=30, default="work", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"


class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# admin.site.register(Product, ProductViewSerializer)
