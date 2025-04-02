import csv

# with open('users.csv', 'r') as file:
#     reader = csv.reader(file)

#     #Let's look at the content of the file
#     for row in reader:
#         print(row)

#Function that displays Main Menu
def display_member_menu():
    # Display a Member Management Menu
    #1. Display All the Member
    #2. Add a new member
    #3. Display Library Card for a Member
    print("******* MEMBER MANAGEMENT MENU *******")
    print("1. Display All Members")
    print("2. Add A New Member")
    print("3. View Library Card")
    print("4. Back to Main Menu")

def add_new_member():
    #Ask user to add details of new member
    mid = input("Enter Member ID: ")
    name = input("Enter name of member: ")
    dob = input("Enter date of birth: ")
    join_date = input("Enter Join Date: ")
    expiry_date = input("Enter Expiry Date: ")
    address = input("Enter Address")

    #Create a new dictionary with input data
    newMember = [mid, name, dob, join_date, expiry_date, address]

    with open('users.csv', 'w') as membersFromFile:
        memberWriter = csv.writer(membersFromFile)
        memberWriter.writerow(newMember)
    

def display_all_members():
    #Display all the members
    print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
        "MID", "NAME", "DOB", "JOIN DATE", "EXP DATE", "ADDRESS"
    ))
    print("-"*80)

    #Open File
    with open('users.csv', 'r') as usersFile:
        membersFromFile = csv.reader(usersFile)
        next(membersFromFile)

        for member in membersFromFile:
            print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
                member[0],
                member[1],
                member[2],
                member[3],
                member[4],
                member[5]
            ))
    # for member in members:
    #     print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
    #         member["MID"],
    #         member["name"],
    #         member["DOB"],
    #         member["join_date"],
    #         member["expiry_date"],
    #         member["address"]
    #     ))
#MAIN PROGRAM STARTS

def member_management_loop():
    #Main Function Loop
    while True:
        display_member_menu()

        # Ask the user to choose an option: (1-3)
        choice = int(input("Enter your choice (1-4): "))

        #IF condition
        if choice == 1:
            display_all_members()
        elif choice == 2:
            add_new_member()
        elif choice == 3:
            #Ask user for member ID, and display library card
            print("Here I will display Library card")
        elif choice == 4:
            break
        else:
            #Display error message
            print("Invalid Choice!")
