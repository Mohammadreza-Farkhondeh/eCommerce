from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .permissions import IsGrantedOrReadOnlyProduct


class ProductViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing products.
    """
    permission_classes = [IsGrantedOrReadOnlyProduct, ]
    queryset = Product.objects.all()
    lookup_field = "slug"

    # Define a dictionary of serializers for different actions
    serializers = {
        "list": ProductListSerializer,
        "detail": ProductDetailSerializer,
    }

    # Override the get_serializer_class method to return the appropriate serializer
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["detail"])


class CategoryViewSet(ViewSet):
    """
    A ViewSet for:
        - list categories
        - detail category (products and categories in the category)
        - create, update, destroy category
    """
    permission_classes = [IsGrantedOrReadOnlyProduct, ]

    def list(self, request):
        """
        get all Categories
        """
        # get all the categories
        queryset = Category.objects.all()
        # serialize them with the CategorySerializer
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, slug=None):
        """
        get products in a Category
        """
        # get the category by its primary key
        category = get_object_or_404(Category, slug=slug)
        # serialize the category
        category_serializer = CategorySerializer(category)
        # get the products of the category or any of its subcategories
        products = Product.objects.by_category(category)
        # serialize the products
        product_serializer = ProductListSerializer(products, many=True)
        # get the subcategories of the category
        subcategories = category.category_set.all()
        # serialize the subcategories
        subcategory_serializer = CategorySerializer(subcategories, many=True)
        # create a dictionary with the category, product and subcategory data
        category_data = {
            "category": category_serializer.data,
            "products": product_serializer.data,
            "subcategories": subcategory_serializer.data
        }
        # return a response with the dictionary
        return Response(category_data, status.HTTP_200_OK)

    def create(self, request):
        """
        Create a new Category
        """
        # create a new category from the request data
        serializer = CategorySerializer(data=request.data)
        # validate the data and save the category
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error response if the data is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        """
        Update an existed Category
        """
        # get the category to update by its primary key
        category = get_object_or_404(Category, slug=slug)
        # update the category with the request data
        serializer = CategorySerializer(category, data=request.data)
        # validate the data and save the category
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return an error response if the data is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, slug=None):
        """
        Update a Category
        """
        # get the category to update by its primary key
        category = get_object_or_404(Category, slug=slug)
        # update the category with the partial request data
        serializer = CategorySerializer(category, data=request.data, partial=True)
        # validate the data and save the category
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return an error response if the data is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        """
        Delete a Category
        """
        # get the category to delete by its primary key
        category = get_object_or_404(Category, slug=slug)
        # delete the category
        category.delete()
        # return a success response
        return Response(status=status.HTTP_204_NO_CONTENT)
