from bs4 import BeautifulSoup

class Product:

    def __init__(self):
        """Represents a product object with a title (str) and a collection
        of technical specs (dict)."""
        self._title = None
        self._specs = {}

    def get_title(self) -> str:
        """Returns product title."""
        return self._title

    def get_specs(self) -> dict:
        """Returns product specs."""
        return self._specs

    def update_title(self, soup: object) -> None:
        """
        Takes in a BeautifulSoup object and extracts the name of the product
        from it. Saves name of product to self._title.

        : param soup: BeautifulSoup object
        """
        # Hash syntax in select() when searching an id
        self._title = soup.select("#product-page-title")[0].get_text("|", True)

    def update_specs(self, soup: object) -> None:
        """
        Takes in a BeautifulSoup object and extracts the technical specs from
        it. Saves tech specs as dictionary in self._specs.

        :param soup: BeautifulSoup object
        """
        # Lists of headers and their corresponding specs, not formatted
        # Dot syntax in select() when searching a class
        headers_li = soup.select(".tech-specs__header")
        specs_li = soup.select(".tech-specs__value")

        # Properly formatted headers & specs without extra chars
        headers_li = [header.get_text("|", True) for header in
                      headers_li]
        specs_li = [spec.get_text("|", True) for spec in specs_li]

        # Create product's spec dict
        for i in range(len(headers_li)):
            self._specs[headers_li[i]] = specs_li[i]
