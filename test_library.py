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

# def test_return_book():
#     library = Library()
#     book = Book("1034-4", "November 9", "Collen Hoover", 2015)
#     library.add_book(book)
#     library.borrow_book("1034-4")
#     library.return_book(book)
#     assert book in library.books  # Book should be available again

def test_view_available_books():
    library = Library()
    book1 = Book("1034-4", "November 9", "Collen Hoover", 2015)
    book2 = Book("3770-8", "my Gita", "Devdutt Pattanaik", 2016)
    library.add_book(book1)
    library.add_book(book2)
    available_books = library.view_available_books()
    assert book1 in available_books
    assert book2 in available_books
