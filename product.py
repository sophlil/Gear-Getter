from bs4 import BeautifulSoup

class Product:

    def __init__(self):
        """Represents a product object with a title (str) and a collection
        of technical specs (dict)."""
        self._title = None
        self._specs = None

    def update_title(self, soup: object) -> str:
        """
        Takes in a BeautifulSoup object and extracts the name of the product
        from it. Saves name of product to self._title. Returns self._title.

        :param soup: BeautifulSoup object
        : return: Product title, str
        """
        # Hash syntax in select() when searching an id
        self._title = soup.select("#product-page-title")[0].get_text("|", True)
        return self._title

    def update_specs(self, soup: object) -> dict:
        """
        Takes in a BeautifulSoup object and extracts the technical specs from
        it. Saves tech specs as dictionary in self._specs. Returns self._specs.

        :param soup: BeautifulSoup object
        :return: Product's tech specs, dict.
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
        self._specs = {self._specs[headers_li[i]]: specs_li[i] for i in
                       range(len(headers_li))}

        return self._specs