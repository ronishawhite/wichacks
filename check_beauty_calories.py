import csv
# import requests
import json
# hardcoded dish
import requests

Dish = "Rustic Italian Tortellini Soup"
# function to extract ingredients
def ReturnIngredientList(Dish):
    with open("Recipes.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for ingredient in reader:
            if ingredient[0] == Dish:
                return ingredient[9]
# ingredientstr = (ReturnIngredientList(Dish))
# print(ingredientstr)
# ingredientArr = ingredientstr.split(",")
# make get requests to Wegmans 1st search API
def WegmanSearch(ingredient):
    URL = "https://api.wegmans.io/products/search?query="+ingredient+"&api-version=2018-10-18&Subscription-Key=12a8aa35602741a2b73a15b9eb77f828"
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    return data["results"][0]["sku"]
# print(WegmanSearch("pasta"))
def WegmanDetail(sku):
    URL = "https://api.wegmans.io/products/"+sku+"?api-version=2018-10-18&Subscription-Key=12a8aa35602741a2b73a15b9eb77f828"
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    return data["nutrients"][1]["quantity"]
def FinalCals(Dish):
    ingredientstr = (ReturnIngredientList(Dish))
    ingredientArr = ingredientstr.split(",")
    Cal = 0
    for ingredient in ingredientArr:
        #     print(ingredient)
        CalsInIng = int(WegmanDetail(WegmanSearch(str(ingredient))))
        #     print(CalsInIng)
        Cal = Cal + CalsInIng
    #     print("Amount of Calories in one serving of "+Dish+ " is: "+ str(Cal))
    return Cal
