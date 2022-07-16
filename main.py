from bs4 import BeautifulSoup
import requests
from link_manager import LinkManager
from pymongo import MongoClient
import certifi
from credentials import *

# Connection string to Mongodb Atlas Cluster
connection = 'mongodb+srv://' + MDB_USERNAME + ':' + MDB_PASSWORD +\
             '@clustergg.4h3xryh.mongodb.net/?retryWrites=true&w=majority'

# Connects to cluster with necessary certificates. Sets an env variable to tell
# OpenSSL where to find root certificates
client = MongoClient(connection, tlsCAFile=certifi.where())

CATEGORIES = ["hiking-backpacks", "tents",
                              "sleeping-bags-and-accessories",
                              "sleeping-pads-cots-and-hammocks",
                              "camp-kitchen", "camp-furniture",
                              "water-bottles-and-treatment",
                              "camp-lighting", "camp-electronics",
                              "gadgets", "health-and-safety",
                              "climbing-shoes", "climbing-harnesses",
                              "climbing-ropes", "webbing-and-cords",
                              "climbing-hardware", "climbing-essentials",
                              "mountaineering-gear"]

# Create new DB on cluster called 'Products'
mdb = client.Products

# Create new collection for DB 'Products' called 'backpacks'
backpacks = mdb.backpacks

# Create prefix to add to search page links
search_prefix = "https://www.rei.com/c/"

# Returns response code from request
response = requests.get(search_prefix + 'backpacking-packs')

# Represents html content from response
soup = BeautifulSoup(response.content, "html.parser")

# Create link manager
lm = LinkManager()

# Find links to all products from search page
lm.search_page_links(soup)

# Extract product details from each link on search page and save them in db
lm.add_products_db(backpacks)


# TO DO:
# - Design of MDB? What product info should be stored? In what way should it
# be stored?
# - Create Search(?) object or functions to handle finding product links,
# adding products to db, looping through links on search page
