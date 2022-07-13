
class Database:

    def __init__(self):
        """Represents a database that holds products and their corresponding
        technical specs. The database is an dictionary with product titles
        (str) as the keys and product objects as the values."""
        self._db = {}

    def get_db(self) -> dict:
        """Returns the whole database."""
        return self._db

    def update_db(self, key: str, value: object) -> None:
        """
        Adds a key/value pair to the db. Key should be string of product's
        title and value should be product object.

        :param key: Product title, str
        :param value: Product object
        """
        self._db[key] = value
