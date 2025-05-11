class Book:
    def __init__(self,title, author, year, ):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False
    def checkout(self):
      self.is_checked_out = True
    def return_book(self):
      self.is_checked_out = False

    def __str__(self):
     return f"{self.title} by {self.author} ({self.year}) (Checked out: {self.is_checked_out})"
    
class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)
    def list_books(self):
        for book in self.collection:
            print(book) 
    def  find_book(self,title) :
        for book in self.collection:
            if book.title.lower() == title.lower():  # Compare titles case-insensitively
                return book
        return None  # If no book is found with the title
       
# Create a Library instance
library = Library()

 # Menu for user interaction
def main():
    while True:
        print("\nLibrary System:")
        print("1. Add a Book")
        print("2. List Books")
        print("3. Find a Book")
        print("4. Checkout a Book")
        print("5. Return a Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Add a book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            new_book = Book(title, author, year)
            library.add_book(new_book)
            print(f"Book '{title}' added to the library.")

        elif choice == "2":
            # List all books
            library.list_books()

        elif choice == "3":
            # Find a book by title
            title = input("Enter the title of the book to search for: ")
            book = library.find_book(title)
            if book:
                print(f"Found: {book}")
            else:
                print("Book not found.")

        elif choice == "4":
            # Checkout a book
            title = input("Enter the title of the book to checkout: ")
            book = library.find_book(title)
            if book and not book.is_checked_out:
                book.checkout()
                print(f"Book '{title}' checked out.")
            elif book and book.is_checked_out:
                print(f"Book '{title}' is already checked out.")
            else:
                print("Book not found.")

        elif choice == "5":
            # Return a book
            title = input("Enter the title of the book to return: ")
            book = library.find_book(title)
            if book and book.is_checked_out:
                book.return_book()
                print(f"Book '{title}' returned.")
            elif book and not book.is_checked_out:
                print(f"Book '{title}' wasn't checked out.")
            else:
                print("Book not found.")

        elif choice == "6":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 6.")

# Start the program
main()
