class LibraryProperty:
    """Class to manage library properties, including books and users."""
    
    def __init__(self):
        """Initializes a new library with no books and no users."""
        self.books = {}  # Dictionary to hold book objects with ISBN as the key
        self.users = []  # List to hold registered users

    def add_book(self, book):
        """Adds a book to the library.
        
        :param book: BookInformation object to add
        """
        self.books[book.isbn] = book  # Store the book using its ISBN as the key

    def remove_book(self, book):
        """Removes a book from the library.
        
        :param book: BookInformation object to remove
        """
        if book.isbn in self.books:
            del self.books[book.isbn]  # Remove the book using its ISBN

    def register_user(self, user):
        """Registers a new user in the library.
        
        :param user: UserRecord object to register
        """
        self.users.append(user)  # Add the user to the list of registered users

    def borrow_book(self, user, book):
        """Allows a user to borrow a book from the library.
        
        :param user: UserRecord object who wants to borrow the book
        :param book: BookInformation object to borrow
        """
        if book.isbn in self.books and book.status == 'Available':  # Check if the book is available
            user.borrow_book(book)

    def return_book(self, user, book):
        """Allows a user to return a borrowed book to the library.
        
        :param user: UserRecord object who is returning the book
        :param book: BookInformation object to return
        """
        if book.isbn in self.books:  # Check if the book is in the library
            user.return_book(book)

    def view_available_books(self):
        """Returns a list of books that are currently available for borrowing."""
        return [book for book in self.books.values() if book.status == 'Available']  # List of available books

    def view_borrowed_books(self):
        """Returns a list of books that are currently borrowed."""
        return [book for book in self.books.values() if book.status == 'Borrowed']  # List of borrowed books

    def __str__(self):
        """Returns a string representation of the library status."""
        return f"Library has {len(self.books)} books and {len(self.users)} registered users."
