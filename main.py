from bs4 import BeautifulSoup
import requests
from database import Database

# Returns response code from request
response_code = requests.get(
    "https://www.rei.com/product/168251/rei-co-op-trailbreak-60-pack-mens")

# Represents html content from response
response_html = response_code.content
soup = BeautifulSoup(response_html, "html.parser")

# Product title
# Hash syntax in select() when searching an id
title = soup.select("#product-page-title")[0].get_text("|", True)
Database.set_db(title)

# Tech specs list of headers
# Dot syntax in select() when searching a class
headers_li = soup.select(".tech-specs__header")

headers_li = [header.get_text("|", True) for header in headers_li]


# TO DO:
# - Figure out DB schema. Dict within Dict? List within List? List within Dict?
# - Eventually loop through all URL's on REI search page
# - Use time module to slow things down?






