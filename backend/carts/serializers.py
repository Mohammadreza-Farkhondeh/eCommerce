from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductListSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["total"]


class CartItemSerializer(serializers.ModelSerializer):
    # use a nested serializer to show the product details
    product = ProductListSerializer(read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "subtotal"]