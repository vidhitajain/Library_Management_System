# test_library.py
import pytest
from library import Library, Book

# def test_add_book():
#     library = Library()
#     book = Book("1034-4", "November 9", "Collen Hoover", 2015)
#     library.add_book(book)
#     assert book in library.books  # Check if the book was added

# def test_borrow_book():
#     library = Library()
#     book = Book("1034-4", "November 9", "Collen Hoover", 2015)
#     library.add_book(book)
#     borrowed_book = library.borrow_book("1034-4")
#     assert borrowed_book == book  # Check if the borrowed book is correct
#     assert book not in library.books  # Book should be removed 

def test_return_book():
    library = Library()
    book = Book("1034-4", "November 9", "Collen Hoover", 2015)
    library.add_book(book)
    library.borrow_book("1034-4")
    library.return_book(book)
    assert book in library.books  # Book should be available again
