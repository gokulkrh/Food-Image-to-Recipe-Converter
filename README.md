# Food-Image-to-Recipe-Converter
<a href="https://colab.research.google.com/drive/1TnX3rEkcR11njx0--v-2msGwgRokLbro?usp=sharing">Colab notebook</a>

This project implements a food image to recipe converter for Indian food. 

## Dataset
The dataset used in this project can be obtained by running the `scraper.py` script.

All the recipes in this dataset are scraped from <a href="https://www.food.com/">food.com</a> with "Indian" as search term. A total of 786 unique Indian recipes are taken from the website.

The recipes from the website are scraped and saved as a JSON file, google_images_download library is used to download images. For each recipe 10 images are downloaded for training and 2 for testing.

A total of 9432 images are downloaded (7860 train and 1572 test)

## Method
This is a fairly complicated task, I mean humans use several senses like sight, smell and taste to differentiate between food, an algorithm can't do that, well at least not yet, and on top of that a lot of Indian dishes look the same (hey, even a human can't tell the difference between "chicken curry" and "chicken tikka masala" just by looking at it).

Running the `generate_encodings.py` script encodes each image and saves it in encodings.txt along with the corresponding recipe names in enc_names.txt.

The input image is first encoded and then the cosine similarity between the image vector and images in the dataset are calculated, now due to the reasons mentioned earlier, a total of 10 predictions will be taken for each image and if at least one of them is correct, well YAY!!.

Densenet201 was used to encode the images, out of all the models tested, this showed the highest accuracy (58%), which is pretty decent for this task, you know, because of the stuff mentioned before.

## SeeFood Website
<img src="SeeFood/WebApp/static/WebApp/title.png" width="500">

The web application is made using django.

You can upload a food image or, on mobile, you can take a picture. The system fetches 4 recipes that are visually most similar to the uploaded image, if your not happy with the result there is an option to show 4 more reciepes.
<br><br>
![](https://github.com/gokulkrh/Food-Image-to-Recipe-Converter/blob/main/mobile_demo.gif)<br>
This is a demo of the web application on mobile devices.

In the above example a picture of a vegetable puffs are taken and the application gave the correct recipe.
<br><br><br>

<b>Please NOTE:</b> For anyone asking about the links.csv file, I have intentionally not uploaded that file as it contains direct links to the recipes in food.com website, which i felt might be a little too much,

but if you are trying to recreate this project you don't need the links.csv file, the data scrapped using links.csv is in `indian_recipes.json` file, use this file to get recipe names and modify the `scaper.py` file to only download the images for each recipe.
<br><br><br>
**reference:** http://pic2recipe.csail.mit.edu/
