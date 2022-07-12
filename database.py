
class Database:
    def __init__(self):
        self._db = {}

    def get_db(self) -> dict:
        return self._db

    def set_db(self, key: str, value: dict=None) -> None:
        if value is None:
            self._db[key] = {}
        self._db[key] = value



