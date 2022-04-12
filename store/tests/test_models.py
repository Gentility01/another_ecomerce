from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(title='book', slug='book')

    def test_category_model_entry(self):
        """
        Test Category models data insertion/types/fields attribute
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_models_entry(self):
        """
        Test Category models return name
        """

        data = self.data1
        self.assertEqual(str(data), 'book')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(title='book', slug='book')
        User.objects.create(username='douglas')
        self.data1 = Product.objects.create(category_id=1, title='django', created_by_id=1,
                                            slug='django', prices='20.00', image='download_1')

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django')

    # def test_product_model_entry(self): 1:14:50
    #     data = self.data1
    #     self.assertEqual(str(data), 'django')
