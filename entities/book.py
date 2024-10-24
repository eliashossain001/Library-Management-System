class BookInformation:
    """Class to represent information about a book."""
    
    def __init__(self, title, author, isbn):
        """
        Initializes a new instance of BookInformation.
        
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"  # Status indicating whether the book is available for borrowing

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Status: {self.status}"
