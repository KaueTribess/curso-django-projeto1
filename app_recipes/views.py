from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from app_recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
                is_published=True
            ).order_by('-id')
    
    
    return render(request=request, template_name='recipes/pages/home.html', context={
        'recipes': recipes,
    })


def categories(request, category_id): 
    recipes = get_list_or_404(
        Recipe, Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id'))

    return render(request=request, template_name='recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} | '
    })


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe, pk=id, is_published=True
        )
    
    return render(request=request, template_name='recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
