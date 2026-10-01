# Create a Book class with attributes title, author, is_available
# Create methods: displayBookDetails, lend_book-->is_available=False, return_book --> is_available=True

# Create object to call the set methods.

class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

    def insertBook(self):  # book1.insertBook()
        with open("day11/book.txt", "a") as file:
            file.write(f"{self.title},{self.author},{self.is_available}\n")
        print("Book saved into file.")

    def lendBook(self):  # self --> book(abc,Adam,True) Book that is to be lent
        # --['XYZ,Adam,True', 'ABC,Adam,True', 'STR,Adam,False']
        if not self.is_available:
            print("The book isn't available to be lent at the moment.")
        all_books = loadBooks()

        for i in range(len(all_books)):  # 0,1,2
            book_detail = all_books[i].split(",")  # -->['abc','Adam',True]
            # all_books[1]='ABC,Adam,True' -->string
            if book_detail[0].lower() == self.title.lower():
                book_detail[2] = "False"
                all_books[i] = ",".join(book_detail)
                # all_books[1]=,.join(['ABC','Adam',False])
        # all_books=['XYZ,Adam,True', 'ABC,Adam,False', 'STR,Adam,False']

        with open("day11/book.txt", "w") as file:
            for book in all_books:
                file.write(f"{book}\n")
        print("Here's your book. Please return it by September 30.")

    def returnBook(self):
        if self.is_available:
            print("The book hasn't been rent. Something went wrong")
        else:
            print("Thank you for returning the book.")
            self.is_available = True


def findBook(title):  # xyz
    books = loadBooks()
    print(books)
    for item in books:  # item --> 'XYZ,Adam,True'
        book_details = item.split(",")  # -->['XYZ','Adam','True']

        if (book_details[0].lower() == title.lower()):

            book = Book(book_details[0], book_details[1],
                        True if book_details[2] == "True" else False)

            return book

    return None


def loadBooks():
    final_list = []
    with open("day11/book.txt", "r") as file:
        text = file.read()
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
        choice = int(input("Enter  a choice(1-5): "))

        if (choice == 5):
            break
        elif (choice == 1):
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
            book = findBook(title=title)  # title:abc
            # book is an object with attributes-->abc,Adam,True
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


# Update Logic:
# --ask user input for which book to update
# -- find the book, if found return a book object else None
# -- load every line of the file as an element of an all_books list
# -- Iterate over every line in the file to find the title to update
# -- Spilt every line by "," so that we can access every element as a list
# -- If file's title and input title matches then update the required value
# -- Update that particular index of the all_books list with the updated value using join function
# -- Write the all_books into the file in "w" mode of access
