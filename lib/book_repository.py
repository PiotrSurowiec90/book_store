from lib.book import Book


class BookRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        query = "SELECT * FROM books;"
        rows = self._connection.execute(query)
        return [
            Book(row.get("id"), row.get("title"), row.get("author_name"))
            for row in rows
        ]
