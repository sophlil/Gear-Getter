from product import Product
from bs4 import BeautifulSoup
import requests
from time import sleep
import pymongo

class LinkManager:

    def __init__(self):
        self._search_links = ["hiking-backpacks", "tents",
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
        self._links = []
        self._prefix = "https://www.rei.com"

    def search_page_links(self, soup: BeautifulSoup) -> None:
        # Gather all a tags from search page
        link_el = soup.find_all('a')

        # Create a list of links for products only, getting the attribute val
        # of 'href' for each a tag
        for el in link_el:
            link = el["href"]
            if link[0:9] == '/product/':
                self._links.append(self._prefix + link)

    def add_products_db(self, db: pymongo) -> None:
        # Extract product details from each link on search page and save them in db
        for link in self._links:
            response = requests.get(link)
            bs_obj = BeautifulSoup(response.content, "html.parser")

            # Creates Product object and updates title/specs of product
            product = Product()
            product.update_title(bs_obj)
            product.update_weight(bs_obj)

            # Adds title/weight to MDB
            add = {product.get_title(): product.get_weight()}
            db.insert_one(add)

            # Delay requests to 1 req/second
            sleep(1)
