from django.test import TestCase
from carts.models import Cart, CartItem
from products.models import Product
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()
faker = Faker()



class TestCartTotalUpdate(TestCase):
    def setUp(self):
        import carts.receivers
        # create a user and a cart for the user
        self.user = User.objects.create(email=faker.email())
        self.cart, _ = Cart.objects.get_or_create(user=self.user, total=0)
        self.product1 = Product.objects.create(name=faker.name(), price=100)
        self.product2 = Product.objects.create(name=faker.name(), price=200)

    def test_cart_total_should_update_when_cart_item_is_created(self):
        # create a cart item for product 1 with quantity 2
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        # check that the cart total is updated to 200
        self.assertEqual(self.cart.total, 200)

    def test_cart_total_should_update_when_cart_item_is_modified(self):
        # create a cart item for product 1 with quantity 2
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        # modify the cart item quantity to 3
        cart_item.quantity = 3
        cart_item.save()
        # check that the cart total is updated to 300
        self.assertEqual(self.cart.total, 300)

    def test_cart_total_should_update_when_cart_item_is_deleted(self):
        # create a cart item for product 1 with quantity 2
        cart_item = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        # create another cart item for product 2 with quantity 1
        cart_item2 = CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)
        # check that the cart total is 400
        self.assertEqual(self.cart.total, 400)
        # delete the first cart item
        cart_item.delete()
        # check that the cart total is updated to 200
        self.assertEqual(self.cart.total, 200)
