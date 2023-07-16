from rest_framework.serializers import ModelSerializer, ImageField, SlugField
from .models import Product, Category, ProductImages

# TODO: replace ModelSerializer with HyperlinkedModelSerializer


class ProductListSerializer(ModelSerializer):
    """
    Serializer for list action
    """
    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'image']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"


class ProductDetailSerializer(ModelSerializer):
    """
    serializer for actions other than list
    """
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ["name", "slug", "price", "description", "is_available", "images"]


class CategoryListSerializer(ModelSerializer):
    """
    serializer for list action
    """
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent']


class CategoryDetailSerializer(ModelSerializer):
    """
    serializer for actions other than list
    """
    products = ProductListSerializer(many=True, read_only=True)
    subcategories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent', 'products', 'subcategories']