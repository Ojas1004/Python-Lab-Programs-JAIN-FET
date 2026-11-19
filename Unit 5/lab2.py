class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C programming"]

    def display_books(self):
        print("Available books:", self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")


# Creating an object
library = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book = input("Enter book name to borrow: ")
        library.borrow_book(book)

    elif choice == "3":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "4":
        print("Exiting Library System")
        break

    else:
        print("Invalid choice!")