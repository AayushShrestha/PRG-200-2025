members = [
    { "MID": "M001", "name": "John Doe", "DOB": "1999-08-01", "join_date": "2025-01-01", "expiry_date": "2025-01-01", "address": "New Baneshwor"},
    { "MID": "M002", "name": "Rajesh Hamal", "DOB": "1992-08-01", "join_date": "2025-01-01", "expiry_date": "2025-01-01", "address": "Bharatpur"},
    { "MID": "M003", "name": "Rishi Dhamala", "DOB": "1994-08-01", "join_date": "2025-01-01", "expiry_date": "2025-01-01", "address": "Gorkha"},
    { "MID": "M004", "name": "Jyoti Magar", "DOB": "1993-08-01", "join_date": "2025-01-01", "expiry_date": "2025-01-01", "address": "Durbarmarg"},
]

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
    print("4. Exit Application")

def add_new_user():
    #Ask user to add details of new member
    mid = input("Enter Member ID: ")
    name = input("Enter name of member: ")
    dob = input("Enter date of birth: ")
    join_date = input("Enter Join Date: ")
    expiry_date = input("Enter Expiry Date: ")
    address = input("Enter Address")

    #Create a new dictionary with input data
    newMember = {
        "MID": mid,
        "name": name,
        "DOB": dob,
        "join_date": join_date,
        "expiry_date": expiry_date,
        "address": address
    }
    return newMember

def display_all_members():
    #Display all the members
    print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
        "MID", "NAME", "DOB", "JOIN DATE", "EXP DATE", "ADDRESS"
    ))
    print("-"*80)
    for member in members:
        print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
            member["MID"],
            member["name"],
            member["DOB"],
            member["join_date"],
            member["expiry_date"],
            member["address"]
        ))
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
            newMember = add_new_user()
            members.append(newMember)
        elif choice == 3:
            #Ask user for member ID, and display library card
            print("Here I will display Library card")
        elif choice == 4:
            break
        else:
            #Display error message
            print("Invalid Choice!")
