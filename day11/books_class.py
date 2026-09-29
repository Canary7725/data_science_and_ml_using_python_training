# Create a Book class with attributes title, author, is_available
# Create methods: displayBookDetails, lend_book-->is_available=False, return_book --> is_available=True

# Create object to call the set methods.

class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

    def insertBook(self):
        with open("day11/book.txt", "a") as file:
            file.write(f"{self.title},{self.author},{self.is_available}\n")
        print("Book saved into file.")

    def lendBook(self):
        books = loadBooks()
        print(self.is_available)
        if not self.is_available:
            print("The book has already been lent. It is not available at the moment.")
            return
        for i in range(len(books)):
            book_detail = books[i].split(",")

            if book_detail[0].lower() == self.title.lower():
                book_detail[2] = "False"
                books[i] = ",".join(book_detail)
                break

        with open("day11/book.txt", "w") as file:
            for book in books:
                file.write(f"{book}\n")
        print("Here's your book. Please return it by September 30.")

    def returnBook(self):
        if self.is_available:
            print("The book hasn't been rent. Something went wrong")
        else:
            print("Thank you for returning the book.")
            self.is_available = True


def findBook(title):
    books = loadBooks()

    for item in books:
        book_details = item.split(",")

        if (book_details[0].lower() == title.lower()):

            book = Book(book_details[0], book_details[1],
                        True if book_details[2] == "True" else False)

            return book


def loadBooks():
    final_list = []
    with open("day11/book.txt", "r") as file:
        text = file.read()
        # print(text.split("\n"))
        final_list = text.split("\n")
        final_list = [item for item in final_list if len(item) > 2]
        return final_list


def displayAllBooks():
    books_list = loadBooks()
    for item in books_list:
        book_detail_list = item.split(",")
        print(f"""
        Title: {book_detail_list[0]}
        Author: {book_detail_list[1]}
        is_available:{book_detail_list[2]}
        -------------------------
        """)
# ['XYZ,Adam,True', 'ABC,Adam,False', 'STR,Adam,True']


menu = """
    1. Insert Book
    2. Display Book Details
    3. Lend Book
    4. Return Book
    ----------------
    5. Exit
"""

while True:
    print(menu)
    try:
        choice = int(input("Enter  a choice(1-4): "))

        if (choice == 5):
            break
        if (choice == 1):
            title = input("Enter title of the book: ")
            author = input("Enter author of the book: ")
            availability = input("Is the book available?(Y/N): ")
            is_available = True if availability.lower() == 'y' else False
            book1 = Book(title, author, is_available)
            book1.insertBook()

        elif (choice == 2):
            displayAllBooks()

        elif (choice == 3):
            title = input("Enter book title to lend: ")
            book = findBook(title=title)

            if book is None:
                print("Book Not Found in file")
            else:
                book.lendBook()

        elif (choice == 4):
            book1.returnBook()

        else:
            raise ValueError
    except ValueError:
        print("Please enter a integer between 1 and 4.")
