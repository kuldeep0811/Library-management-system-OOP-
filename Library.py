class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "added to library")

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(book_name, "issued")
        else:
            print(book_name, "is not available")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "returned to library")

    def display_books(self):
        if self.books:
            print("Available books:", self.books)
        else:
            print("No books available")


# Creating Library object
lib = Library()

# Adding books
lib.add_book("Python")
lib.add_book("Java")
lib.add_book("C++")

# Issuing book
lib.issue_book("Python")

# Returning book
lib.return_book("Python")

# Displaying books
lib.display_books()
