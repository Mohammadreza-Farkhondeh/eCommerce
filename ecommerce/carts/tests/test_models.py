import pytest
from carts.models import Cart, CartItem
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError


@pytest.mark.django_db
def test_cart_model_normal(user):
    cart = Cart.objects.create(
        user=user,
        total=0.00
    )
    assert cart.id is not None
    assert cart.user == user
    assert cart.total == 0.00


@pytest.mark.django_db
def test_cart_model_bad_user():
    user = AnonymousUser
    with pytest.raises(ValueError):
        cart = Cart.objects.create(
            user=user,
            total=0.00
        )
        assert cart.id is None
        assert cart.user != user
        assert cart.total != 100


@pytest.mark.django_db
def test_cart_model_bad_total(user):
    with pytest.raises(IntegrityError):
        cart = Cart.objects.create(
            user=user,
            total=-10.0
        )
        assert cart.id is None
        assert cart.user == user
        assert cart.total != -10.0


@pytest.mark.django_db
def test_cart_item_normal(product, cart):
    cart_item = CartItem.objects.create(
        product=product,
        cart=cart,
        quantity=1,
        subtotal=10
    )
    assert cart_item.id is not None
    assert cart_item.product == product
    assert cart_item.cart == cart
    assert cart_item.subtotal == 10.0


@pytest.mark.django_db
def test_cart_item_bad_quantity(product, cart):
    with pytest.raises(IntegrityError):
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=-1,
            subtotal=10
        )
        assert cart_item.id is None
        assert cart_item.product != product
        assert cart_item.cart != cart
        assert cart_item.subtotal != 10.0


@pytest.mark.django_db
def test_cart_item_bad_quantity(product, cart):
    with pytest.raises(IntegrityError):
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
            subtotal=-10
        )
        assert cart_item.id is None
        assert cart_item.product != product
        assert cart_item.cart != cart
        assert cart_item.subtotal != 10.0
