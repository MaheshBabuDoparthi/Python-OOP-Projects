# Project 3: Library Management System (OOP)
# Author: Mahesh Babu Doparthi

class Library:

    def __init__(self, book_name, author, book_id, available):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id
        self.available = available

    def show_book(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Book ID:", self.book_id)
        print("Available:", self.available)

    def issue_book(self):
        if self.available == "Yes":
            self.available = "No"
            print("Book Issued Successfully")
        else:
            print("Book Not Available")

    def return_book(self):
        if self.available == "No":
            self.available = "Yes"
            print("Book Returned Successfully")
        else:
            print("Book is Already Available")

    def search_book(self, book_name):
        if self.book_name == book_name:
            print("Book Found!")
        else:
            print("Book Not Found!")


# Creating Objects

book1 = Library("Python Basics", "Mahesh", 101, "Yes")
book2 = Library("Java Programming", "Rahul", 102, "Yes")

print("========== Book 1 ==========")
book1.show_book()

print("\nSearching for Python Basics")
book1.search_book("Python Basics")

print("\nIssuing Book")
book1.issue_book()
book1.show_book()

print("\nReturning Book")
book1.return_book()
book1.show_book()

print("\n========== Book 2 ==========")
book2.show_book()

print("\nSearching for C Programming")
book2.search_book("C Programming")