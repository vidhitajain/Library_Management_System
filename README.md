# Library Management System

## Project Overview
The **Library Management System** allows users to add, borrow, return, and view available books. 

## Features
- **Add Books**: Users can add books with unique ISBNs, titles, authors, and publication years.
- **Borrow Books**: Users can borrow books if they are available.
- **Return Books**: Users can return borrowed books.
- **View Available Books**: Users can view all available books in the library.

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/vidhitajain/Library_Management_System.git<br>
cd Library_Management_System

### 2.Set Up a Virtual Enviornment(Optional)

python -m venv venv<br>
venv\Scripts\activate

### 3. Install Required Dependencies

pip install -r requirements.txt

### 4. Running the Tests

pytest --tb=short --disable-warnings

### 5. Running the Project

Although this project doesn't include a user interface, you can interact with the Library class via Python scripts

Example:
from library import Library<br>

library = Library()<br>
available_books = library.available_books()<br>

for book in available_books:<br>
    print(f"{book.title} by {book.author} ({book.publication_year})")<br>
