from rest_framework.viewsets import ViewSet
from .models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CartItemSerializer
from products.models import Product


class CartViewSet(ViewSet):
    """
    A ViewSet for acting with cart
    """
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'slug'

    def get_queryset(self):
        # get the current user
        user = self.request.user
        # return only the cart items that belong to the user's cart
        return CartItem.objects.filter(cart__user=user)

    def get_cart(self):
        cart = Cart.objects.get(user=self.request.user)
        return cart

    def list(self, request):
        """
        list all cart items in the user cart
        """
        queryset = self.get_queryset()
        serializer = CartItemSerializer(queryset, many=True)
        total = Cart.objects.filter(user=request.user).first().total
        data = {
            'total': total,
            'items': serializer.data
        }
        return Response(data)

    def create(self, request):
        """
        post to /cart/ to add an item to cart
        """
        cart = self.get_cart()
        product = request.data.get("product")
        print()
        # check if the product exists and is available
        if product and Product.objects.filter(slug=product["slug"], is_available=True).exists():
            product = Product.objects.get(slug=product["slug"])
            # get the quantity from the request data or default to 1
            quantity = request.data.get("quantity", 1)
            # check if the cart already has an item with this product
            if cart.cartitem_set.filter(product=product).exists():
                cart_item = cart.cartitem_set.get(product=product)
                # update the quantity
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # create a new cart item with the product, quantity and subtotal
                cart_item = CartItem.objects.create(
                    product=product,
                    cart=cart,
                    quantity=quantity,
                    subtotal=product.price * quantity
                )
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # return an error response if the product is not valid or available
            return Response({"error": "Invalid or unavailable product"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, slug=None):
        """
        update cart item
        """
        cart_item = get_object_or_404(CartItem, product__slug=slug)
        quantity = request.data.get("quantity")
        if quantity and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        """
        delete an item from cart
        """
        queryset = self.get_queryset()
        cart_item = queryset.filter(product__slug=slug).first()
        if cart_item:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:  # if the item does not exist
            return Response(status=status.HTTP_404_NOT_FOUND)
