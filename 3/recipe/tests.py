from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")
        self.assertIn("Desserts", list(iter(category)))