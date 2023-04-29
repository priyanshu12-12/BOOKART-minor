from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer, Product, Requirments


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.shop_url = reverse('shop')
        self.require_url = reverse('require')
        self.product = Product.objects.create(name='Product 1', description='Product 1 description', img='product1.jpg')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_shop_GET(self):
        response = self.client.get(self.shop_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')

    def test_require_POST(self):
        response = self.client.post(self.require_url, {
            'name': 'John Doe',
            'number': 1234567890,
            'bookname': 'Book 1',
            'edition': 'First Edition'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Requirments.objects.filter(name='John Doe', number=1234567890, bookname='Book 1', edition='First Edition').exists())

    def test_purchase_GET(self):
        response = self.client.get(reverse('purchase', args=[self.product.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'purchase.html')
        self.assertEquals(response.context['product'], self.product)
