from backbone import *

def start_banking():
    text2 = """Welcome to the Horizon Bank!
    Enter 1 if you are a new customer.
    Enter 2 if you are an existing customer.
    Enter 3 To Check Data [Admin Only] !.
    Enter 4 to terminate the application.\n"""
    print(text2)
    choice2 = input("Enter Your Request-> ")
    while not choice2 in ('1', '2', '3') or int_check(choice2) is False:
        print("Invalid Input!")
        choice2 = input("Please Enter Either 1 , 2 OR 3 Only-> ")
    match int(choice2):
        case 1:
            new_user()
        case 2:
            existing_user()
        case 3:
            check_data()
        case 4:
            exit()

if __name__ == '__main__':
    start_banking()