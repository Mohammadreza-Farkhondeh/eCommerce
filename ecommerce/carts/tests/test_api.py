from rest_framework.test import APIClient, APITestCase
from products.models import Product
from carts.models import Cart, CartItem
from products.serializers import ProductListSerializer
from django.contrib.auth import get_user_model
import pytest

from faker import Faker
faker = Faker()


@pytest.mark.usefixtures("user")
class CartViewSetTestCase(APITestCase):

    @pytest.mark.django_db
    def setUp(self):
        self.user = get_user_model().objects.create(
        email=faker.email(),
    )
        self.product = Product.objects.create(
            name=faker.name(),
            slug=faker.word(),
            price=10.00,
            image="test.jpg",
            description="This is a test product.",
            category=None,
        )
        self.product2 = Product.objects.create(
            name=faker.name(),
            slug=faker.word(),
            price=20.00,
            image="test2.jpg",
            description="This is a test product2.",
            category=None,
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.cart, _ = Cart.objects.get_or_create(user=self.user, total=10)
        self.cart_item = CartItem.objects.create(
            product=self.product,
            cart=self.cart,
            quantity=1,
            subtotal=10.00)

    def test_list_cart_items(self):
        response = self.client.get("/api/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["items"]), 1)
        self.assertEqual(response.data["items"][0]["product"]['name'], self.product.name)
        self.assertEqual(response.data["items"][0]["quantity"], 1)

    def test_create_cart_item_normal(self):
        response = self.client.post("/api/cart/", {'slug': self.product2.slug, 'quantity': 1})
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["product"], ProductListSerializer(self.product))
        self.assertEqual(response.data["quantity"], 1)
