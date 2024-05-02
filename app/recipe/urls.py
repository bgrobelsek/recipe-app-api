"""
URL mappings for recipe app
"""
from django.urls import (
    path,
    include, 
    reverse
)

from rest_framework.routers import DefaultRouter
from recipe import views

from recipe.views import RecipeViewSet, TagViewSet, IngredientViewSet  # Import the missing classes

router = DefaultRouter()
router.register('recipes', RecipeViewSet)  # Use the imported class
router.register('tags', TagViewSet)  # Use the imported class
router.register('ingredients', IngredientViewSet)  # Use the imported class

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]


def detail_url(recipe_id):
    """Return the URL for the recipe detail endpoint"""
    return reverse('recipe:recipe-detail', args=[recipe_id])
