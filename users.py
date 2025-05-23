import csv

#Function that displays Main Menu
def display_member_menu():
    # Display a Member Management Menu
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

    with open('users.csv', 'a') as membersFromFile:
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

def display_card_format(member):
    #Print Card ko Design
    print("+" + "-"*50 + "+")
    print("|          IDENTITY CARD          |")
    print("+" + "-"*20 + "+")
    print("ID        : " + member[0] + " |")
    print("Name      : " + member[1] + " |")
    print("DOB       : " + member[2] + " |")
    print("Join Date : " + member[3] + " |")
    print("Expiry    : " + member[4] + " |")
    print("Addres    : " + member[5] + " |")

def display_library_card(memberId):
    #Open the file
    with open('users.csv', 'r') as membersFromFile:
        reader = csv.reader(membersFromFile)
        next(reader)
        for member in reader:
            currentMemberId = member[0]
            if currentMemberId == memberId:
                #We got the right row, now display library card
                display_card_format(member)
                break
    #Find the right row using memberID
    #Display that row in a card format

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
            # print("Here I will display Library card")
            memberId = input("Enter Member ID: ")
            display_library_card(memberId)
        elif choice == 4:
            break
        else:
            #Display error message
            print("Invalid Choice!")
