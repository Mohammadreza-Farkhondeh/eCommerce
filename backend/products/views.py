from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import *
from .models import Product, Category
from .permissions import IsGrantedOrReadOnlyProduct


class ProductViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing products.
    """
    permission_classes = [IsGrantedOrReadOnlyProduct, ]
    queryset = Product.objects.all()
    lookup_field = "slug"
    search_fields = ['name']
    filterset_fields = ['price', 'category']
    ordering_fields = ['price', 'created']

    # Define a dictionary of serializers for different actions
    serializers = {
        "list": ProductListSerializer,
        "detail": ProductDetailSerializer,
    }

    # Override the get_serializer_class method to return the appropriate serializer
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["detail"])


class CategoryViewSet(ModelViewSet):
    """
    A ViewSet for:
        - list categories
        - detail category (products and categories in the category)
        - create, update, destroy category
    """
    permission_classes = [IsGrantedOrReadOnlyProduct, ]
    queryset = Category.objects.all()
    lookup_field = "slug"
    filterset_fields = ['parent']

    # Define a dictionary of serializers for different actions
    serializers = {
        "list": CategoryListSerializer,
        "detail": CategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["detail"])
