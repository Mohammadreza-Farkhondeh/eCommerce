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
        response = self.client.post("/api/cart/", {'product': {'slug': self.product2.slug}}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["product"]['slug'], self.product2.slug)
        self.assertEqual(response.data["product"]['price'], self.product2.price)
        self.assertEqual(response.data["quantity"], 1)
        self.assertEqual(float(response.data['subtotal']), self.product2.price)

    def test_create_cart_item_exist(self):
        response = self.client.post("/api/cart/", {'product': {'slug': self.product.slug}}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["product"]['slug'], self.product.slug)
        self.assertEqual(response.data["product"]['price'], self.product.price)
        self.assertEqual(response.data["quantity"], 2)
        self.assertEqual(float(response.data['subtotal']), self.product.price)

    def test_create_cart_product_unavailable(self):
        self.product.is_available = False
        self.product.save()
        response = self.client.post("/api/cart/", {'product': {'slug': self.product.slug}}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 400)

    def test_update_cart_item_normal(self):
        response = self.client.patch(f"/api/cart/{self.product.slug}/", {'quantity': 5})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["product"]['slug'], self.product.slug)
        self.assertEqual(response.data["product"]['price'], self.product.price)
        self.assertEqual(response.data["quantity"], 5)

    def test_update_cart_item_bad_quantity(self):
        print(f"api/cart/{self.product.slug}")
        response = self.client.patch(f"/api/cart/{self.product.slug}/", {})
        print(response)
        self.assertEqual(response.status_code, 400)

    def test_delete_Cart_item(self):
        response = self.client.delete(f"/api/cart/{self.product.slug}/")

        self.assertEqual(response.status_code, 204)
        cart_item = CartItem.objects.filter(product=self.product).first()
        self.assertIsNone(cart_item)

    def test_delete_Cart_item_not_exist(self):
        response = self.client.delete(f"/api/cart/{self.product.slug}aaa/")

        self.assertEqual(response.status_code, 404)
        cart_item = CartItem.objects.filter(product=self.product).first()
        self.assertIsNotNone(cart_item)