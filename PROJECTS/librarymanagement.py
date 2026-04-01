library = []

def add_book(title, author):
    book = {"title": title, "author": author, "status": "available"}
    library.append(book)

def display_books():
    if not library:
        print("Library is empty")
    else:
        for i, book in enumerate(library, start=1):
            print(i, book["title"], "-", book["author"], "-", book["status"])

def borrow_book(title):
    for book in library:
        if book["title"].lower() == title.lower() and book["status"] == "available":
            book["status"] = "borrowed"
            return
    print("Book not available")

def return_book(title):
    for book in library:
        if book["title"].lower() == title.lower() and book["status"] == "borrowed":
            book["status"] = "available"
            return
    print("Book not borrowed")

def main():
    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            add_book(title, author)
        elif choice == "2":
            display_books()
        elif choice == "3":
            title = input("Book to borrow: ")
            borrow_book(title)
        elif choice == "4":
            title = input("Book to return: ")
            return_book(title)
        elif choice == "5":
            break

main()
