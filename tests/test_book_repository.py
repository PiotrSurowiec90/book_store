from lib.book_repository import BookRepository
from lib.book import Book


def test_get_all_books(db_connection):
    """ Test all returns list of book objects fom db"""
    db_connection.seed("seeds/book_store.sql")
    book_repo = BookRepository(db_connection)
    all_books = book_repo.all()
    expected = [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell' ),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

    assert all_books == expected