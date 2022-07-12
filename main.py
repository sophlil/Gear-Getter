from bs4 import BeautifulSoup
import requests
from database import Database

# Create DB object
# Keys: Product titles Values: Dicts containing spec key/val pairs
db = Database()

# Returns response code from request
response_code = requests.get(
    "https://www.rei.com/product/168251/rei-co-op-trailbreak-60-pack-mens")

# Represents html content from response
response_html = response_code.content
soup = BeautifulSoup(response_html, "html.parser")

# Product title
# Hash syntax in select() when searching an id
title = soup.select("#product-page-title")[0].get_text("|", True)

# Add product title as key in db
db.set_db(title)

# Lists of headers and their corresponding specs
# Dot syntax in select() when searching a class
headers_li = soup.select(".tech-specs__header")
specs_li = soup.select(".tech-specs__value")

# Properly formatted headers & specs without extra chars
headers_li = [header.get_text("|", True) for header in headers_li]
specs_li = [spec.get_text("|", True) for spec in specs_li]

# Create product's spec dict to add to db
product_specs = {}
for i in range(len(headers_li)):
    product_specs[headers_li[i]] = specs_li[i]

# Complete product info in db
db.set_db(title, product_specs)

print(db.get_db())



# TO DO:
# - Use OOP principles/encapsulation to segment code into different functions
#   and files
# - Eventually loop through all URL's on REI search page
# - Use time module to slow things down?
