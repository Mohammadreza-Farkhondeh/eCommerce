from rest_framework.serializers import ModelSerializer, ImageField
from .models import Product

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
    serializer for action other than list
    """
    image = ImageField(use_url=True)  # or False so only give relative url

    class Meta:
        model = Product
        fields = "__all__"
