from models.library import Library

def main():
    lib = Library()

    lib.add_book("The Alchemist", "Paulo Coelho", "111", "Fiction", 5)
    lib.add_book("Clean Code", "Robert C. Martin", "222", "Programming", 3)

    lib.add_borrower("Alice", "alice@example.com", "M001")
    lib.add_borrower("Bob", "bob@example.com", "M002")

    lib.borrow_book("M001", "111")
    lib.return_book("M001", "111")

    print("\nSearch results for 'code':")
    for book in lib.search_books("code"):
        print(book)

if __name__ == "__main__":
    main()
