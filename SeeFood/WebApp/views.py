import base64
import string
import os
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from PIL import Image
from .encoder import get_recipes
import json


def home_page(request):
    raw_image = None
    uploaded_image = None
    recipe_list_to_return = []
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            raw_image = form.cleaned_data['image']
            uploaded_image = base64.b64encode(raw_image.file.read()).decode('ascii')
            raw_image = Image.open(raw_image)
            recipe_list = get_recipes(raw_image)
            path_to_json = os.path.join(settings.BASE_DIR, 'WebApp/static/WebApp/indian_recipes.json')
            x = json.load(open(path_to_json))

            for i in range(len(recipe_list)):
                name = recipe_list[i]
                y = list(filter(lambda x: x["name"] == name, x))
                if len(y) != 0:
                    y = y[0]
                    image_link = "WebApp/display_images/" + name + "1.jpg"
                    calories = y['calories']
                    cooking_time = y['cooking_time']
                    ingredients = y['ingredients']
                    directions = y['directions']
                    list_to_append = [string.capwords(name), image_link, calories, cooking_time, ingredients, directions]
                    recipe_list_to_return.append(list_to_append)

    else:
        form = ImageUploadForm()
    return render(request, 'WebApp/home.html', {'form': form, 'uploaded_image': uploaded_image,
                                                'recipe_list_to_return': recipe_list_to_return[:4],
                                                'similar_recipe_list': recipe_list_to_return[4:10]})
