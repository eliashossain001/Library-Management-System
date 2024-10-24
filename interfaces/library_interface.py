class LibraryInterface:
    def add_book(self, book):
        raise NotImplementedError

    def remove_book(self, book):
        raise NotImplementedError

    def register_user(self, user):
        raise NotImplementedError

    def borrow_book(self, user, book):
        raise NotImplementedError

    def return_book(self, user, book):
        raise NotImplementedError

    def view_available_books(self):
        raise NotImplementedError

    def view_borrowed_books(self):
        raise NotImplementedError
