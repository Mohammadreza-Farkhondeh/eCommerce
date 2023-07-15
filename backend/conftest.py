import pytest
from django.contrib.auth import get_user_model
from products.models import Product, Category
from carts.models import Cart, CartItem

from faker import Faker
faker = Faker()


@pytest.fixture
def user():
    return get_user_model().objects.create(
        email=faker.email(),
    )



@pytest.fixture
def category():
    return Category.objects.create(
        name=faker.word(),
        parent=None
    )


@pytest.fixture
def sub_category(category):
    return Category.objects.create(
        name=faker.word(),
        parent=category,
    )


@pytest.fixture
def product(category):
    return Product.objects.create(
            name=faker.word(),
            price=10.00,
            image=faker.file_name(extension="jpg"),
            description=faker.text(),
            category=category,
        )


@pytest.fixture
def cart(user):
    return Cart.objects.create(
        user=user,
        total=0
    )


@pytest.fixture
def cart_item(product, cart):
    return CartItem.objects.create(
        product=product,
        cart=cart,
        quantity=1,
        subtotal=10
    )