from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class ShopViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('shop')
        self.product1 = Product.objects.create(name='Product 1', description='Description for product 1', img='images/product1.jpg')
        self.product2 = Product.objects.create(name='Product 2', description='Description for product 2', img='images/product2.jpg')

    def test_shop_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product1.description)
        self.assertContains(response, self.product2.name)
        self.assertContains(response, self.product2.description)
