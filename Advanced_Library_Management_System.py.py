# Project 10: Advanced Library Management System
# Author: Mahesh Babu Doparthi

class Book:

    def __init__(self, book_name, author, book_id):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id

    def show_details(self):
        print("📖 Book Name:", self.book_name)
        print("✍️ Author:", self.author)
        print("🆔 Book ID:", self.book_id)

    def issue_book(self):
        print("✅ Book Issued Successfully!")

    def return_book(self):
        print("✅ Book Returned Successfully!")

    def search_book(self, book_id):
        if self.book_id == book_id:
            print("✅ Book Found!")
        else:
            print("❌ Book Not Found!")

    def delete_book(self):
        print("🗑️ Book Deleted Successfully!")


books = []

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        book_id = int(input("Enter Book ID: "))

        book = Book(book_name, author, book_id)
        books.append(book)

        print("✅ Book Added Successfully!")

    elif choice == 2:

        if len(books) == 0:
            print("No Books Available!")
        else:
            for book in books:
                book.show_details()
                print("------------------------")

    elif choice == 3:

        search_id = int(input("Enter Book ID: "))
        found = False

        for book in books:
            if book.book_id == search_id:
                book.show_details()
                found = True
                break

        if not found:
            print("❌ Book Not Found!")

    elif choice == 4:

        search_id = int(input("Enter Book ID: "))

        for book in books:
            if book.book_id == search_id:
                book.issue_book()
                break
        else:
            print("❌ Book Not Found!")

    elif choice == 5:

        search_id = int(input("Enter Book ID: "))

        for book in books:
            if book.book_id == search_id:
                book.return_book()
                break
        else:
            print("❌ Book Not Found!")

    elif choice == 6:

        search_id = int(input("Enter Book ID: "))

        for book in books:
            if book.book_id == search_id:
                books.remove(book)
                book.delete_book()
                break
        else:
            print("❌ Book Not Found!")

    elif choice == 7:
        print("🙏 Thank You for Using Library Management System!")
        break

    else:
        print("❌ Invalid Choice!")