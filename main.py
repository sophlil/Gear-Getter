from bs4 import BeautifulSoup
import requests
from database import Database
from time import sleep
from product import Product

# Create DB object
# Keys: Product titles Values: Product objects
db = Database()

# Create prefix to add to links
prefix = "https://www.rei.com"

# Returns response code from request
response = requests.get("https://www.rei.com/c/backpacking-packs")

# Represents html content from response
soup = BeautifulSoup(response.content, "html.parser")

# Gather all link elements from search page
link_el = soup.find_all('a')

# Create a list of links for products only
links = []
for el in link_el:
    link = el["href"]
    if link[0:9] == '/product/':
        links.append(prefix + link)

# Extract product details from each link on search page and save them in db
for link in links:
    response = requests.get(link)
    bs_obj = BeautifulSoup(response.content, "html.parser")

    # Creates Product object and updates title/specs of product
    product = Product()
    product.update_title(bs_obj)
    title = product.get_title()
    product.update_specs(bs_obj)

    # Add product to db as product title: product object key/val pairs
    db.update_db(title, product)

    # Delay requests to 1 req/second
    sleep(1)

print(db.get_db().keys())
print(db.get_db()['Co-op Cycles DRT 1.1 Bike'].get_specs())


# TO DO:
# - Set up actual DB for scraper
# - Create Search(?) object to handle finding product links, adding products to
# db, looping through links on search page
