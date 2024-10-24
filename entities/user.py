from abc import ABC, abstractmethod

class AbstractUser(ABC):
    """Abstract class to define user behaviors."""

    @abstractmethod
    def borrow_book(self, book):
        """Method to borrow a book."""
        pass

    @abstractmethod
    def return_book(self, book):
        """Method to return a book."""
        pass

class UserRecord(AbstractUser):
    """Class to represent a regular user in the library."""
    
    def __init__(self, name, identification_number):
        """
        Initializes a new instance of UserRecord.
        
        :param name: Name of the user
        :param identification_number: Unique identification number for the user
        """
        self.name = name
        self.identification_number = identification_number
        self.borrowed_books = []  # List to hold borrowed books

    def borrow_book(self, book):
        """Allows the user to borrow a book.
        
        :param book: BookInformation object to borrow
        """
        if isinstance(book, list):  # Check if the input is a list of books
            for b in book:  # Iterate through the list of books
                b.status = "Borrowed"  # Update book status to 'Borrowed'
                self.borrowed_books.append(b)  # Add book to borrowed list
        else:  # If a single book is passed
            book.status = "Borrowed"
            self.borrowed_books.append(book)

    def return_book(self, book):
        """Allows the user to return a borrowed book.
        
        :param book: BookInformation object to return
        """
        book.status = "Available"  # Update book status to 'Available'
        self.borrowed_books.remove(book)  # Remove book from borrowed list

    def __str__(self):
        """Returns a string representation of the user's borrowed books."""
        borrowed_titles = [book.title for book in self.borrowed_books]  # List of borrowed book titles
        return f"User: {self.name}, ID: {self.identification_number}, Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"

class AdminUser(UserRecord):
    """Class to represent an admin user with additional privileges."""
    
    def __init__(self, name, identification_number):
        """Initializes a new instance of AdminUser."""
        super().__init__(name, identification_number)
    
    def add_book(self, library, book):
        """Allows the admin to add a book to the library.
        
        :param library: LibraryProperty object where the book will be added
        :param book: BookInformation object to add
        """
        library.add_book(book)
        print(f"{self.name} added '{book.title}' to the library.")
    
    def remove_book(self, library, book):
        """Allows the admin to remove a book from the library.
        
        :param library: LibraryProperty object from which the book will be removed
        :param book: BookInformation object to remove
        """
        library.remove_book(book)
        print(f"{self.name} removed '{book.title}' from the library.")
    
    def __str__(self):
        """Returns a string representation of the admin user."""
        return f"Admin User: {self.name}, ID: {self.identification_number}, Can add/remove books."
