#Display A Welcome Screen that says "Welcome to Library Management"
#Display Main Menu
# - 1. Manage Members
# --- Show Member Management Menu
# --- 1. Add Member
# --- 2. Display All Members
# --- 3. Remove a Member
# --- 4. Display Library Card
# --- 5. Back
# - 2. Manage Books
# --- 1. Add Book
# --- 2. Display All Books
# --- 3. Remove a Book
# --- 4. Back
# - 3. Borrow a Book
# - 4. Lend a Book
# - 5. Exit 

import users

def display_main_welcome_screen():
    print("*"*50)
    print("**", " Welcome To Library Management System ", '**')
    print("*"*50)

def display_main_menu():
    print("******* MAIN MENU *******")
    print("1. Manage Members")
    print("2. Manage Books")
    print("3. Lend A Book")
    print("4. Return A Book")
    print("5. Exit Application")

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
            # user_management_loop()
            print("Choice 2")
        elif choice == 3:
            # borrow_book()
            print("Choice 3")
        elif choice == 4:
            # lend_book()
            print("Choice 4")
        elif choice == 5:
            break
        else:
            print("Invalid Choice! Try Again!")

#Run Main Function
main()