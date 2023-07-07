from django.db.models import signals
from django.dispatch import receiver
from .models import Cart, CartItem
from django.conf import settings


# define a signal to update the subtotal of a cart item when it is created or modified
@receiver(signals.post_save, sender=CartItem)
def update_subtotal(sender, instance, **kwargs):
    instance.subtotal = instance.product.price * instance.quantity
    instance.save()


# define a signal to update the total of a cart when a cart item is created, modified, or deleted
@receiver(signals.post_save, sender=CartItem)
@receiver(signals.post_delete, sender=CartItem)
def update_total(sender, instance, **kwargs):
    cart = instance.cart
    # sum the subtotals of all the cart items in the cart
    cart.total = sum(int(cartitem.subtotal) for cartitem in cart.cartitem_set.all())
    # save the cart
    cart.save()


# define a signal to create a cart for a user when the user is created
@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_cart(sender, instance, created, **kwargs):
    # check if the user is newly created
    if created:
        # create a new cart for the user with zero total
        Cart.objects.create(user=instance, total=0)
