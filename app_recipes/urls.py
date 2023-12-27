from django.urls import path
from app_recipes.views import home

urlpatterns = [
    path('', home),
]