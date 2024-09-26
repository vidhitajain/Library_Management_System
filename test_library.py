# test_library.py
import pytest
from library import Library, Book

def test_add_book():
    library = Library()
    book = Book("1034-4", "November 9", "Collen Hoover", 2015)
    library.add_book(book)
    assert book in library.books  # Check if the book was added