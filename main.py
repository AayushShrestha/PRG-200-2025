
import users
import books

def display_main_welcome_screen():
    print("*"*50)
    print("**", " Welcome To Library Management System ", '**')
    print("*"*50)

def display_main_menu():
    print("******* MAIN MENU *******")
    print("1. Manage Members")
    print("2. Manage Books")
    print("3. Exit Application")

def main():

    display_main_welcome_screen()
    
    #Main Program Loop
    while True:
        display_main_menu()

        #Take input from user 1-5
        choice = int(input("Enter a choice (1-5): "))

        if choice == 1:
            users.member_management_loop()
        elif choice == 2:
            books.book_management_loop()
        elif choice == 3:
            print("Thank you. See you again!")
            break
        else:
            print("Invalid Choice! Try Again!")

#Run Main Function
main()