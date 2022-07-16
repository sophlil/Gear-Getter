from bs4 import BeautifulSoup
import requests
from database import Database
from time import sleep
from product import Product
from pymongo import MongoClient
import certifi
from credentials import *

# Connection string to Mongodb Atlas Cluster
connection = 'mongodb+srv://' + MDB_USERNAME + ':' + MDB_PASSWORD +\
             '@clustergg.4h3xryh.mongodb.net/?retryWrites=true&w=majority'

# Connects to cluster with necessary certificates
client = MongoClient(connection, tlsCAFile=certifi.where())

# Create new DB on cluster called 'Products'
mdb = client.Products

# Create new collection for DB 'Products' called 'backpacks'
backpacks = mdb.backpacks

# Create DB object
# Keys: Product titles Values: Product objects
# db = Database()

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
    product.update_specs(bs_obj)

    # Adds title/spec dict to MDB
    add = {product.get_title(): product.get_specs()}
    backpacks.insert_one(add)

    # Add product to db as product title: product object key/val pairs
    # db.update_db(title, product)

    # Delay requests to 1 req/second
    sleep(1)


# TO DO:
# - Set up actual DB for scraper
# - Create Search(?) object to handle finding product links, adding products to
# db, looping through links on search page
