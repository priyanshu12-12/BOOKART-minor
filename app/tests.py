from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Customer.objects.create(username='testuser', password='testpassword', email='testuser@test.com')
        
    def test_customer_login(self):
        response = self.client.post(reverse('index'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302) # Check that the response is a redirect
        self.assertRedirects(response, '/home/') # Check that the response redirects to the correct page

    def test_customer_registration(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpassword', 'email': 'newuser@test.com'})
        self.assertEqual(response.status_code, 302) # Check that the response is a redirect
        self.assertRedirects(response, '/') # Check that the response redirects to the correct page

    def test_shop_page(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200) # Check that the response is successful
        self.assertContains(response, self.user.username) # Check that the response contains the username of the test user

    def test_require_page(self):
        response = self.client.post(reverse('require'), {'name': 'Test User', 'number': '1234567890', 'bookname': 'Test Book', 'edition': '1st'})
        self.assertEqual(response.status_code, 200) # Check that the response is successful
        self.assertTrue(response.context['form'].is_valid()) # Check that the form is valid
