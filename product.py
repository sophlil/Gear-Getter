from bs4 import BeautifulSoup

class Product:

    def __init__(self):
        """Represents a product object with a title (str), a collection
        of technical specs (dict), and a weight (str)."""
        self._title = None
        self._weight = ' '
        self._specs = {}

    def get_title(self) -> str:
        """Returns product title."""
        return self._title

    def get_specs(self) -> dict:
        """Returns product specs."""
        return self._specs

    def get_weight(self) -> str:
        """Returns product weight."""
        return self._weight

    def update_title(self, soup: BeautifulSoup) -> None:
        """
        Takes in a BeautifulSoup object and extracts the name of the product
        from it. Saves name of product to self._title.

        :param soup: BeautifulSoup object
        """
        # Hash syntax in select() when searching an id
        self._title = soup.select("#product-page-title")[0].get_text("|", True)

    def update_specs(self, soup: BeautifulSoup) -> None:
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

    def update_weight(self, soup: BeautifulSoup) -> None:
        """
        Takes in a BeautifulSoup object and extracts the weight from it.
        Saves weight as str in self._weight.

        :param soup: BeautifulSoup object
        """
        # Search for all tags that contains tech specs
        elements = soup.find_all(['tr'])
        for el in elements:
            # Get text within elements and format it
            result = el.get_text(" ", True)
            if result[0:6] == "Weight":
                self._weight = result
