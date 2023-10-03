from lib.book import Book


def test_obj_attrs():
    """Test Attrs"""

    book = Book(1, "Title", "Author")
    assert book.id == 1
    assert book.title == "Title"
    assert book.author_name == "Author"


def test_two_books_same_attrs():
    """Test two equal books"""

    book = Book(1, "Title", "Author")
    book2 = Book(1, "Title", "Author")
    assert book == book2


def test_obj_repr():
    """Test __repr__"""

    book = Book(1, "Title", "Author")
    result = str(book)
    assert result == "Title by Author"