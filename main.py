from use_cases.library import LibraryProperty
from entities.book import BookInformation
from entities.user import UserRecord, AdminUser

def main():
    """Main function to run the library management system."""
    
    # Initialize the library
    library = LibraryProperty()

    # Create instances of books with their titles, authors, and ISBNs
    book1 = BookInformation("1984", "George Orwell", "1234567890")
    book2 = BookInformation("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = BookInformation("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

    # Add the book instances to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create user instances for a regular user and an admin user
    user1 = UserRecord("Alice", "001")
    admin1 = AdminUser("Charlie", "admin001")

    # Register the users in the library
    library.register_user(user1)
    library.register_user(admin1)

    # Admin adds a new book to the library
    book4 = BookInformation("Brave New World", "Aldous Huxley", "1234567891")
    admin1.add_book(library, book4)

    # User borrows a book from the library
    library.borrow_book(user1, book1)

    # Display available books in the library
    print("Available books:")
    available_books = library.view_available_books()
    if available_books:  # Check if there are available books
        print("\n".join(map(str, available_books)))
    else:
        print("No books available.")

    # Display borrowed books in the library
    print("\nBorrowed books:")
    borrowed_books = library.view_borrowed_books()
    if borrowed_books:  # Check if there are borrowed books
        print("\n".join(map(str, borrowed_books)))
    else:
        print("No books borrowed.")

    # User returns a borrowed book
    library.return_book(user1, book1)

    # Display available books after the return
    print("\nAvailable books after return:")
    available_books_after_return = library.view_available_books()
    if available_books_after_return:  # Check if there are available books
        print("\n".join(map(str, available_books_after_return)))
    else:
        print("No books available.")

    # Print the overall status of the library
    print("\n" + str(library))

# Ensure that the main function is executed only when the script is run directly
if __name__ == "__main__":
    main()
