from rest_framework.serializers import ModelSerializer, ImageField, SlugField
from .models import Product, Category

# TODO: replace ModelSerializer with HyperlinkedModelSerializer


class ProductListSerializer(ModelSerializer):
    """
    Serializer for list action
    """
    class Meta:
        model = Product
        fields = ['title', 'price','image']


class ProductDetailSerializer(ModelSerializer):
    """
    serializer for actions other than list
    """
    image = ImageField(use_url=True)  # or False so only give relative url

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    """
    serializer for actions on Category
    """
    slug = SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ["name", "slug"]
        extra_kwargs = {"name": {"write_only": True}}
