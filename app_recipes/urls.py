from django.urls import path
from . import views

#recipes:recipe
app_name = 'app_recipes'


urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/category/<int:category_id>/', views.categories, name="category"),
]