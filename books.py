import csv

#Function that displays Main Menu
def display_books_menu():
    # Display a Books Management Menu
    print("******* BOOKS MANAGEMENT MENU *******")
    print("1. Display All Books")
    print("2. Add A New Book")
    print("3. View Book Details")
    print("4. Back to Main Menu")

def add_new_book():
    #Ask user to add details of new book
    bid = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    publish_date = input("Enter Publish Date: ")
    edition = int(input("Enter Edition Number: "))
    genre = input("Enter Book Genre: ")

    #Create a new dictionary with input data
    newBook = [bid, name, author, publish_date, edition, genre]

    with open('books.csv', 'a') as booksFromFile:
        bookWriter = csv.writer(booksFromFile)
        bookWriter.writerow(newBook)
    

def display_all_books():
    #Display all the books
    print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
        "BID", "NAME", "AUTHOR", "PUBLISH DATE", "EDITION", "GENRE"
    ))
    print("-"*80)

    #Open File
    with open('books.csv', 'r') as booksFile:
        booksFromFile = csv.reader(booksFile)
        next(booksFile)

        for book in booksFromFile:
            print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
                book[0],
                book[1],
                book[2],
                book[3],
                book[4],
                book[5]
            ))

def display_book_format(book):
    print("+" + "-"*50 + "+")
    print("|          BOOK DETAILS          |")
    print("+" + "-"*20 + "+")
    print("ID           : " + book[0] + " |")
    print("Name         : " + book[1] + " |")
    print("Author       : " + book[2] + " |")
    print("Publish Date : " + book[3] + " |")
    print("Edition      : " + book[4] + " |")
    print("Genre        : " + book[5] + " |")

def display_book_details(bookId):
    #Open the file
    with open('books.csv', 'r') as booksFromFile:
        reader = csv.reader(booksFromFile)
        next(reader)
        for book in reader:
            currentBookId = book[0]
            if currentBookId == bookId:
                #We got the right row, now display library card
                display_book_format(book)
                break

#MAIN PROGRAM STARTS
def book_management_loop():
    #Main Function Loop
    while True:
        display_books_menu()

        # Ask the user to choose an option: (1-3)
        choice = int(input("Enter your choice (1-4): "))

        #IF condition
        if choice == 1:
            display_all_books()
        elif choice == 2:
            add_new_book()
        elif choice == 3:
            #Ask user for book ID, and display details
            bookId = input("Enter Book ID: ")
            display_book_details(bookId)
        elif choice == 4:
            break
        else:
            #Display error message
            print("Invalid Choice!")
