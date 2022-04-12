
from unittest import skip
from urllib import request

from django.contrib.auth.models import User
# from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_product


# @skip("demostrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponse(TestCase):
    def setUp(self):
        Category.objects.create(title='book', slug='book')
        User.objects.create(username='douglas')
        self.data1 = Product.objects.create(category_id=1, title='django', created_by_id=1,
                                            slug='django', prices='20.00', image='download_1')

        self.c = Client()
        self.factory = RequestFactory()

    def test_url_allowed_host(self):
        """
        test allowed hosts
        """
        my_response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(my_response.status_code, 400)
        my_response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(my_response.status_code, 200)

    def test_product_detail_test(self):
        my_response = self.c.get(reverse("store:product_detail", args=['django']))
        self.assertEqual(my_response.status_code, 200)

    def test_category_detail_test(self):
        my_response = self.c.get(reverse("store:category_details", args=['book']))
        self.assertEqual(my_response.status_code, 200)

    def test_home_page_html(self):
        my_response = all_product(request)
        html = my_response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(my_response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/item/django-beginers')
        my_response = all_product(request)
        html = my_response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(my_response.status_code, 200)
