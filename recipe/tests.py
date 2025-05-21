from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")
        self.assertIn("Desserts", list(iter(category)))

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Dishes")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Borscht",
            description="Ukrainian beet soup",
            instructions="Boil ingredients together.",
            ingredients="Beets, potatoes, carrots",
            category=self.category
        )
        self.assertEqual(recipe.title, "Borscht")
        self.assertEqual(recipe.category.name, "Main Dishes")
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)