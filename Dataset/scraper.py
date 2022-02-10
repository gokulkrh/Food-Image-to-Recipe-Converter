import requests
import pandas as pd
import json
import re
from bs4 import BeautifulSoup
import os
from google_images_download import google_images_download
import shutil


def downloadimage(recipe_name):
    response = google_images_download.googleimagesdownload()
    args = {"keywords": recipe_name, "format": "jpg", "limit": 12, "output_directory": "downloaded_images"}
    response.download(args)

    parent_dir = "/Dataset/downloaded_images/" + recipe_name + "/"
    train_dir = "/Dataset/train_images"
    test_dir = "/Dataset/test_images"
    images = "/Dataset/images"
    for i, filename in enumerate(os.listdir(parent_dir)):
        dst = recipe_name + str(i) + ".jpg"
        src = parent_dir + filename
        dst1 = parent_dir + dst
        os.rename(src, dst1)
        for j in range(12):
            shutil.copy(dst1, images)
            if i <= 9:
                shutil.copy(dst1, train_dir)
            else:
                shutil.copy(dst1, test_dir)


def getname(raw_text):
    raw_text = raw_text.lower()
    raw_text = re.sub(r"\(.*?\)", "", raw_text)
    raw_text = re.sub(r'[^\w\s]', '', raw_text)
    return raw_text.strip()


def getcalories(soup):
    return soup.find('p', {'class': "recipe-nutrition__item bold"}).text.strip()


def getcookingtime(soup):
    return soup.find('span', {'class': ""}).text.strip()


def getingredients(soup):
    ingredients = soup.find_all('li', {'class': "recipe-ingredients__item"})
    ingredients_string = ""
    for i in ingredients:                                   # add newline after each ingredient.
        ingredients_string += i.text + "\n"
    return ingredients_string


def getdirections(soup):
    directions = soup.find_all('li', {'class': "recipe-directions__step"})
    directions_string = ""
    for i in directions:                                    # add newline after each step.
        directions_string += i.text + "\n"
    return directions_string


def scrapeText(name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    recipe_name = getname(name)
    dicto = {'name': recipe_name, 'cooking_time': getcookingtime(soup), 'calories': getcalories(soup),
             'ingredients': getingredients(soup), 'directions': getdirections(soup)}
    downloadimage(recipe_name)
    return dicto


if __name__ == "__main__":
    links = pd.read_csv("links.csv")
    list_names = links['name']
    list_links = links['links']

    c = 1
    list_of_recipes = []
    for i in range(len(list_names)):
        x = getname(list_names[i])
        print(c, list_names[i], list_links[i])
        list_of_recipes.append(scrapeText(list_names[i], list_links[i]))
        c += 1

    with open('indian_recipes.json', 'w') as f:             # write the scraped data to a JSON file
        json.dump(list_of_recipes, f)
