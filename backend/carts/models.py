from django.db import models
from django.conf import settings
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class Cart(models.Model):
    """
    Cart model
    oneToOne relationship with user
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)


class CartItem(models.Model):
    """
    CartItem model
    FK with Product
    FK with Cart
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
