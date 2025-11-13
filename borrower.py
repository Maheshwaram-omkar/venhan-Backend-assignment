class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = {}

    def __repr__(self):
        return f"{self.name} (ID: {self.membership_id})"

    def update(self, name=None, contact=None):
        if name: self.name = name
        if contact: self.contact = contact
