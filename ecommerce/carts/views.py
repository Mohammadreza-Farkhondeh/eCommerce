from rest_framework.viewsets import ViewSet
from .models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartViewSet(ViewSet):
    """
    A ViewSet for acting with cart
    """
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        # get the current user
        user = self.request.user
        # return only the cart items that belong to the user's cart
        return CartItem.objects.filter(cart__user=user)

    def get_product(self):
        data = self.request.data
        product = Product.objects.get_object_or_404(slug=data.get('slug'))
        return product

    def list(self, request):
        """
        list all cart items in the user cart
        """
        # get the queryset of cart items
        queryset = self.get_queryset()
        # serialize them with the CartItemSerializer
        serializer = CartItemSerializer(queryset, many=True)
        # return a response with the serialized data
        try:
            total =Cart.objects.filter(user=request.user).first().total
        except:
            total = 0
        data = {
            'total': total,
            'items': serializer.data
        }
        return Response(data)

    def create(self, request):
        """
        post to /cart/ to add an item to cart
        """
        # create a new cart item from the request data
        product = self.get_product()
        serializer = CartItemSerializer(data={'product': product, 'quantity': 1})
        # validate the data and save the cart item
        if serializer.is_valid():
            # set the cart of the cart item to the user's cart
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error response if the data is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        """
        update cart item
        """
        # get the queryset of cart items
        queryset = self.get_queryset()
        product = self.get_product()
        data = {'product': product, 'quantity': request.data.get('quantity')}
        # get the cart item to update by its primary key
        cart_item = get_object_or_404(queryset, product=product)
        # update the cart item with the request data
        serializer = CartItemSerializer(cart_item, data=data)
        # validate the data and save the cart item
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return an error response if the data is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        """
        delete an item from cart
        """
        # get the queryset of cart items
        queryset = self.get_queryset()
        product = self.get_product()
        # get the cart item to delete by its primary key
        cart_item = get_object_or_404(queryset, product=product)
        # delete the cart item
        cart_item.delete()
        # return a success response
        return Response(status=status.HTTP_204_NO_CONTENT)
