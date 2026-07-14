"""
Simplified Design a Library Management System
Using Object-Oriented Programming Principles in Python
"""

class Book:
    """Class to represent a book in the library"""
    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} ({status})"


class Patron:
    """Class to represent a library patron (user)"""
    def __init__(self, patron_id, name, email):
        self.patron_id = patron_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Add a book to patron's borrowed list"""
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    def return_book(self, book):
        """Remove a book from patron's borrowed list"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def get_borrowed_books(self):
        """Return list of books borrowed by the patron"""
        return self.borrowed_books
    
    def __str__(self):
        return f"Patron: {self.name} (ID: {self.patron_id})"


class Library:
    """Class to manage the entire library system"""
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []
    
    def add_book(self, book):
        """Add a new book to the library"""
        self.books.append(book)
        print(f"✓ Book added: {book.title}")
    
    def register_patron(self, patron):
        """Register a new patron to the library"""
        self.patrons.append(patron)
        print(f"✓ Patron registered: {patron.name}")
    
    def find_book_by_title(self, title):
        """Find a book by its title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_patron_by_id(self, patron_id):
        """Find a patron by their ID"""
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None
    
    def borrow_book(self, patron_id, book_title):
        """Allow a patron to borrow a book"""
        patron = self.find_patron_by_id(patron_id)
        book = self.find_book_by_title(book_title)
        
        if patron is None:
            print(f"✗ Patron with ID {patron_id} not found.")
            return False
        
        if book is None:
            print(f"✗ Book '{book_title}' not found in the library.")
            return False
        
        if not book.is_available:
            print(f"✗ Book '{book.title}' is currently not available.")
            return False
        
        # Process borrowing
        book.is_available = False
        patron.borrow_book(book)
        print(f"✓ {patron.name} borrowed '{book.title}'")
        return True
    
    def return_book(self, patron_id, book_title):
        """Allow a patron to return a borrowed book"""
        patron = self.find_patron_by_id(patron_id)
        book = self.find_book_by_title(book_title)
        
        if patron is None:
            print(f"✗ Patron with ID {patron_id} not found.")
            return False
        
        if book is None:
            print(f"✗ Book '{book_title}' not found in the library.")
            return False
        
        if book not in patron.get_borrowed_books():
            print(f"✗ {patron.name} has not borrowed this book.")
            return False
        
        # Process return
        book.is_available = True
        patron.return_book(book)
        print(f"✓ {patron.name} returned '{book.title}'")
        return True
    
    def display_all_books(self):
        """Display all books in the library"""
        print("\n" + "="*60)
        print(f"BOOKS IN {self.name.upper()}")
        print("="*60)
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
        print()
    
    def display_all_patrons(self):
        """Display all registered patrons"""
        print("\n" + "="*60)
        print(f"REGISTERED PATRONS IN {self.name.upper()}")
        print("="*60)
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons:
                print(f"{patron} - Borrowed: {len(patron.get_borrowed_books())} book(s)")
        print()
    
    def display_patron_books(self, patron_id):
        """Display books borrowed by a specific patron"""
        patron = self.find_patron_by_id(patron_id)
        
        if patron is None:
            print(f"✗ Patron with ID {patron_id} not found.")
            return
        
        print(f"\n--- Books borrowed by {patron.name} ---")
        borrowed = patron.get_borrowed_books()
        if not borrowed:
            print("No books borrowed.")
        else:
            for book in borrowed:
                print(f"  • {book.title} by {book.author}")
        print()


# ==================== DEMO ====================
def main():
    """Main function to demonstrate the library management system"""
    
    # Create library
    library = Library("City Library")
    
    # Add books to the library
    print("\n--- ADDING BOOKS ---")
    library.add_book(Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5"))
    library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"))
    library.add_book(Book(3, "1984", "George Orwell", "978-0-451-52494-2"))
    library.add_book(Book(4, "Pride and Prejudice", "Jane Austen", "978-0-141-43951-8"))
    library.add_book(Book(5, "The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0"))
    
    # Register patrons
    print("\n--- REGISTERING PATRONS ---")
    library.register_patron(Patron(101, "Alice Johnson", "alice@email.com"))
    library.register_patron(Patron(102, "Bob Smith", "bob@email.com"))
    library.register_patron(Patron(103, "Carol White", "carol@email.com"))
    
    # Display all books and patrons
    library.display_all_books()
    library.display_all_patrons()
    
    # Borrowing operations
    print("\n--- BORROWING BOOKS ---")
    library.borrow_book(101, "The Great Gatsby")
    library.borrow_book(102, "1984")
    library.borrow_book(102, "Pride and Prejudice")
    library.borrow_book(103, "To Kill a Mockingbird")
    
    # Display patron books
    print("\n--- PATRON BOOK STATUS ---")
    library.display_patron_books(101)
    library.display_patron_books(102)
    
    # Display updated book status
    library.display_all_books()
    
    # Returning operations
    print("\n--- RETURNING BOOKS ---")
    library.return_book(101, "The Great Gatsby")
    library.return_book(102, "1984")
    
    # Final display
    library.display_all_books()
    library.display_patron_books(102)
    
    print("\n" + "="*60)
    print("Library Management System Demo Complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
