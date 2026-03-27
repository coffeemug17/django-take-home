from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category, Tag

class ProductSearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Electronics')
        self.tag = Tag.objects.create(name='Sale')

        self.product = Product.objects.create(
            name='Wireless Headphones',
            description='High quality wireless headphones',
            category=self.category
        )
        self.product.tags.add(self.tag)
    
    def test_all_products_displayed_by_default(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Headphones')
        self.assertContains(response, 'Electronics')
        self.assertContains(response, 'Sale')
    
    def test_search_by_description(self):
        response = self.client.get(reverse('product_list'), {'q': 'wireless'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Headphones')
    
    def test_filter_by_category(self):
        response = self.client.get(reverse('product_list'), {'category': self.category.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Headphones')
        self.assertContains(response, 'Electronics')
    
    def test_filter_by_tags(self):
        response = self.client.get(reverse('product_list'), {'tags': [self.tag.id]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Headphones')
        self.assertContains(response, 'Sale')
    
    def test_combined_filters(self):
        response = self.client.get(reverse('product_list'), {
            'q': 'wireless',
            'category': self.category.id,
            'tags': [self.tag.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wireless Headphones')
        self.assertContains(response, 'Electronics')
        self.assertContains(response, 'Sale')

    def test_no_results(self):
        response = self.client.get(reverse('product_list'), {'q': 'nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0 products found')

    def test_multi_tag_and_logic(self):
        tag2 = Tag.objects.create(name='Premium')
        self.product.tags.add(tag2)

        other_product = Product.objects.create(
            name='Basic Product',
            description='A basic product',
            category=self.category
        )
        other_product.tags.add(self.tag)  # only has Sale, not Premium

        response = self.client.get(reverse('product_list'), {
            'tags': [self.tag.id, tag2.id]
        })
        self.assertContains(response, 'Wireless Headphones')  # has both tags
        self.assertNotContains(response, 'Basic Product')