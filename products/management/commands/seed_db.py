from django.core.management.base import BaseCommand
from products.models import Category, Tag, Product


class Command(BaseCommand):
    help = 'Seeds the database with sample categories, tags, and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Product.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Creating categories...')
        electronics = Category.objects.create(name='Electronics')
        clothing = Category.objects.create(name='Clothing')
        books = Category.objects.create(name='Books')
        kitchen = Category.objects.create(name='Kitchen')
        sports = Category.objects.create(name='Sports')

        self.stdout.write('Creating tags...')
        sale = Tag.objects.create(name='Sale')
        new_arrival = Tag.objects.create(name='New Arrival')
        popular = Tag.objects.create(name='Popular')
        wireless = Tag.objects.create(name='Wireless')
        eco_friendly = Tag.objects.create(name='Eco-Friendly')
        limited_edition = Tag.objects.create(name='Limited Edition')
        best_seller = Tag.objects.create(name='Best Seller')
        clearance = Tag.objects.create(name='Clearance')
        premium = Tag.objects.create(name='Premium')
        bundle = Tag.objects.create(name='Bundle')

        self.stdout.write('Creating products...')
        products_data = [
            {
                'name': 'Wireless Headphones',
                'description': 'High quality wireless headphones with noise cancellation and 30 hour battery life',
                'category': electronics,
                'tags': [wireless, popular, best_seller],
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight running shoes with extra cushioning for long distance runs',
                'category': sports,
                'tags': [new_arrival, popular],
            },
            {
                'name': 'Python Programming Book',
                'description': 'Comprehensive guide to Python programming for beginners and intermediate developers',
                'category': books,
                'tags': [best_seller, popular],
            },
            {
                'name': 'Stainless Steel Pan',
                'description': 'Durable stainless steel pan suitable for all stovetops including induction',
                'category': kitchen,
                'tags': [premium, eco_friendly],
            },
            {
                'name': 'Bluetooth Speaker',
                'description': 'Portable waterproof bluetooth speaker with 360 degree sound',
                'category': electronics,
                'tags': [wireless, sale],
            },
            {
                'name': 'Yoga Mat',
                'description': 'Non-slip eco-friendly yoga mat with alignment lines',
                'category': sports,
                'tags': [eco_friendly, new_arrival],
            },
            {
                'name': 'Mystery Novel',
                'description': 'Gripping mystery thriller set in 1920s London',
                'category': books,
                'tags': [sale, popular],
            },
            {
                'name': 'Air Fryer',
                'description': 'Digital air fryer with 8 preset cooking modes and easy clean basket',
                'category': kitchen,
                'tags': [best_seller, new_arrival],
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'Compact mechanical keyboard with RGB backlight and tactile switches',
                'category': electronics,
                'tags': [premium, limited_edition],
            },
            {
                'name': 'Cycling Shorts',
                'description': 'Padded cycling shorts with moisture wicking fabric',
                'category': sports,
                'tags': [sale, clearance],
            },
            {
                'name': 'Self Help Book',
                'description': 'Practical guide to building better habits and achieving long term goals',
                'category': books,
                'tags': [best_seller, bundle],
            },
            {
                'name': 'Coffee Maker',
                'description': 'Programmable coffee maker with built in grinder and thermal carafe',
                'category': kitchen,
                'tags': [premium, popular],
            },
            {
                'name': 'Smartwatch',
                'description': 'Fitness tracking smartwatch with heart rate monitor and GPS',
                'category': electronics,
                'tags': [wireless, new_arrival, premium],
            },
            {
                'name': 'Winter Jacket',
                'description': 'Insulated waterproof winter jacket with detachable hood',
                'category': clothing,
                'tags': [new_arrival, limited_edition],
            },
            {
                'name': 'Cookbook',
                'description': 'Collection of 100 easy weeknight dinner recipes from around the world',
                'category': books,
                'tags': [sale, bundle],
            },
            {
                'name': 'Resistance Bands',
                'description': 'Set of 5 resistance bands with varying tension levels for home workouts',
                'category': sports,
                'tags': [bundle, eco_friendly],
            },
            {
                'name': 'Blender',
                'description': 'High speed blender with stainless steel blades and 6 speed settings',
                'category': kitchen,
                'tags': [sale, clearance],
            },
            {
                'name': 'Denim Jacket',
                'description': 'Classic denim jacket with modern slim fit and stretch fabric',
                'category': clothing,
                'tags': [popular, best_seller],
            },
            {
                'name': 'USB-C Hub',
                'description': '7 in 1 USB-C hub with HDMI 4K output and 100W power delivery',
                'category': electronics,
                'tags': [bundle, clearance],
            },
            {
                'name': 'Linen Trousers',
                'description': 'Breathable linen trousers perfect for warm weather and casual occasions',
                'category': clothing,
                'tags': [eco_friendly, premium],
            },
        ]

        for data in products_data:
            tags = data.pop('tags')
            product = Product.objects.create(**data)
            product.tags.set(tags)

        self.stdout.write(self.style.SUCCESS(
            f'Done: {Category.objects.count()} categories, '
            f'{Tag.objects.count()} tags, '
            f'{Product.objects.count()} products'
        ))