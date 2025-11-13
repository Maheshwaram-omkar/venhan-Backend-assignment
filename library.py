from datetime import datetime, timedelta
from models.book import Book
from models.borrower import Borrower

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}

    def add_book(self, title, author, isbn, genre, quantity):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists. Updating quantity.")
            self.books[isbn].quantity += quantity
        else:
            self.books[isbn] = Book(title, author, isbn, genre, quantity)

    def update_book(self, isbn, **kwargs):
        if isbn in self.books:
            self.books[isbn].update(**kwargs)
        else:
            print("Book not found.")

    def remove_book(self, isbn):
        self.books.pop(isbn, None)

    def add_borrower(self, name, contact, membership_id):
        if membership_id in self.borrowers:
            print("Borrower already exists.")
        else:
            self.borrowers[membership_id] = Borrower(name, contact, membership_id)

    def update_borrower(self, membership_id, **kwargs):
        borrower = self.borrowers.get(membership_id)
        if borrower:
            borrower.update(**kwargs)

    def remove_borrower(self, membership_id):
        self.borrowers.pop(membership_id, None)

    def borrow_book(self, membership_id, isbn, days=14):
        borrower = self.borrowers.get(membership_id)
        book = self.books.get(isbn)

        if not borrower or not book:
            print("Invalid borrower or book.")
            return

        if book.quantity <= 0:
            print("Book not available.")
            return

        book.quantity -= 1
        due_date = datetime.now() + timedelta(days=days)
        borrower.borrowed_books[isbn] = due_date
        print(f"{borrower.name} borrowed '{book.title}', due on {due_date.date()}")

    def return_book(self, membership_id, isbn):
        borrower = self.borrowers.get(membership_id)
        book = self.books.get(isbn)

        if not borrower or isbn not in borrower.borrowed_books:
            print("Invalid return.")
            return

        book.quantity += 1
        due_date = borrower.borrowed_books.pop(isbn)
        overdue = datetime.now() > due_date
        if overdue:
            print(f"Book returned late by {borrower.name}. Please collect fine.")
        else:
            print(f"Book returned on time by {borrower.name}.")

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = [book for book in self.books.values()
                   if keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.genre.lower()]
        return results

    def list_books(self):
        return list(self.books.values())
