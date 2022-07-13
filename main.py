from bs4 import BeautifulSoup
import requests
from database import Database
from time import sleep
from product import Product

# Create DB object
# Keys: Product titles Values: Dicts containing spec key/val pairs
db = Database()

# Returns response code from request
response_code = requests.get(
    "https://www.rei.com/product/168251/rei-co-op-trailbreak-60-pack-mens")

# Represents html content from response
response_html = response_code.content
soup = BeautifulSoup(response_html, "html.parser")

# Creates Product object and sets name of product
product = Product()
title = product.update_title(soup)
specs = product.update_specs(soup)

# Complete product info in db
db.set_db(title, product_specs)

# Delay requests to 1 req/second
sleep(1)


print(db.get_db())



# TO DO:
# - Use OOP principles/encapsulation to segment code into different functions
#   and files
# - Eventually loop through all URL's on REI search page
# - Use time module to slow things down?
