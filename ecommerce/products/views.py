from rest_framework.viewsets import ModelViewSet
from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product


class ProductView(ModelViewSet):
    """
    A ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()

    # Define a dictionary of serializers for different actions
    serializers = {
        "list": ProductListSerializer,
        "detail": ProductDetailSerializer,
    }

    # Override the get_serializer_class method to return the appropriate serializer
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["detail"])
