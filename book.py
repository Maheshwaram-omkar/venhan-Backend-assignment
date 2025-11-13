class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def __repr__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.quantity} available"

    def update(self, title=None, author=None, genre=None, quantity=None):
        if title: self.title = title
        if author: self.author = author
        if genre: self.genre = genre
        if quantity is not None: self.quantity = quantity
