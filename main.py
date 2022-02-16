from SeeFood.WebApp import encoder
from PIL import Image
import json

if __name__ == "__main__":
    img_path = input("path to image: ")
    img = Image.open(img_path)
    recipe_list = encoder.get_recipes(img)
    x = json.load(open("/home/gokul/Projects/Food Image to Recipe Converter/Dataset/indian_recipes.json"))
    print("\n")
    for i in range(5):
        print(i+1, recipe_list[i])
    print("\n")
    n = int(input("Which recipe do you wanna see, Enter number: "))

    y = list(filter(lambda x: x["name"] == recipe_list[n-1], x))
    y = y[0]

    print("\n")
    print(y['name'].capitalize(), "\n")
    print(y['calories'])
    print(y['cooking_time'], "\n")
    print(y['ingredients'], "\n")
    print(y['directions'])