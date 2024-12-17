import random
import pickle
import requests


def fileopen():
    with open("custdata.pkl", "rb") as fp:
        cust_data = pickle.load(fp)
    fp.close()
    return cust_data


def filewrite(x):
    with open("custdata.pkl", "wb") as fp:
        pickle.dump(x, fp)
    fp.close()


cust_data = fileopen()

user_attributes = ["Name", "Govt ID"]
            

def clear():
    crop = False
    while not crop is True:
        try:
            des = int(input("Please Enter The Admin Pin: "))
            if des == 1221:
                file_path = 'custdata.pkl'
                with open(file_path, 'wb') as file:
                    pickle.dump({}, file)
                a = input("Please Press Enter To Exit !")
                break
            else:
                print("Invalid Pin !")
                break
        except:
            print("Invalid Pin Format!")
            exit()


def check_data():
    crop = False
    while not crop is True:
        try:
            des = int(input("Please Enter The Admin Pin: "))
            if des == 1221:
                for i, j in cust_data.items():
                    Name = j["Name"].upper()
                    print(f"{i} : {Name}")
                break
            else:
                print("Invalid Pin !")
                break
        except:
            print("Invalid Pin Format!")
            exit()


def new_ac():
    global cust_data
    a = random.randint(10000, 99999)
    while a in cust_data:
        a = random.randint(10000, 99999)
    return a


def int_check(x):
    try:
        intx = int(x)
    except:
        return False
    else:
        return intx


def phone_check():
    x = input("Please Enter Your Phone Number: ")
    while len(x) < 10 or len(x) >= 11 or int_check(x) is False:
        print("Invalid Number !")
        x = input("Please Enter A 10 Digit Phone NUMBER: ")
    return int(x)


def pin_create():
    x = input("Enter Your Four Digit Pin: ")
    while len(x) < 4 or len(x) >= 5 or int_check(x) is False:
        print("Invalid Value ! The Pin Must Be A 4 Digit NUMBER ONLY !")
        x = input("Please RE-ENTER Your Pin: ")
    return x


def pin_check(ac):
    x = input("Enter Your Four Digit Pin: \n")
    while len(x) < 4 or len(x) >= 5 or int_check(x) is False:
        print("Invalid Value ! The Pin Must Be A 4 Digit NUMBER ONLY !")
        x = input("Please Re-enter your PIN :\t")
    count = 4
    ac = int(ac)
    while x != cust_data[ac]["Four Digit Pin"] and count != 0:
        print("Invalid Pin !")
        print(f"{count} Tries Left !")
        x = input("RE-Enter Your Four Digit Pin: ")
        count -= 1
    if count == 0:
        print("The Account Could Get Locked If You Try Again And Again")
        return False
    else:
        return True


def check_balance(n):
    global cust_data
    return cust_data[int(n)]["Amount"]


def withdraw(ac):
    pin = pin_check(ac)
    ac = int(ac)
    if pin is False:
        print("Trying Multiple Times Could Get Your Account Blocked !")
        exit()
    withdraw = input("\nPlease Enter The Aomunt To Be Withdawn: ")
    while int_check(withdraw) is False:
        print("Invalid Input! Please Enter The Correct Value!")
    while not int(withdraw) < cust_data[ac]["Amount"]:
        print("Insufficient Balance !")
        exit()
    conf = input(f"Are You Sure You Want To Withdraw {withdraw}/- From You Account ? (y or n): ")
    while not conf in ("y", "n"):
        print("You Entered Something Invalid !\n")
        conf = input(f"Are You Sure You Want To Withdraw {withdraw}/- From You Account ? (y or n): ")
    if conf == "y":
        cust_data[ac]["Amount"] -= int(withdraw)
        filewrite(cust_data)
        print(f"Withdrawal Of RS {withdraw}/- Is Successfull !")
        print(f"Your Current Balance Is {check_balance(ac)}")
        exit()
    else:
        print("Operation Canceled By User.")
        exit()


def change_details(ac):
    print("You Will Need To Enter Your Pin In Order To Change Your Personal Details !")
    pin = pin_check(ac)
    ac = int(ac)
    if pin == False:
        print("Invalid Pin Could Not Continue !")
        exit()
    text = f"""\nHii {cust_data[ac]["Name"]}
            Your Govt Id - {cust_data[ac]["Govt ID"]}
            Your Phone Number - {cust_data[ac]["Phone"]}"""
    text2 = f"""\nEnter 1: To Change Your Name
                Enter 2: To Change Your Govt ID
                Enter 3: TO Change Your Phone No.
                Enter 4: To Exit"""
    print(text)
    print(text2)
    choice = input("Please Make your Choice: ")
    while int_check(choice) is False or int(choice) not in (1, 2, 3, 4):
        print("\033cSorry Invalid option selected please try again...\n")
        choice = input("Please Make your Choice: ")
    match int(choice):
        case 1:
            new_name = input("Enter New Name : ")
            cust_data[ac]["Name"] = new_name
            filewrite(cust_data)
            print("Your Name Has Been Changed Successfully !")
            exit()

        case 2:
            govtid = input("Enter New Government ID : ")
            print(f"Your New Govt Id {govtid} Is Updated Successfully")
            cust_data[ac]["Govt ID"] = govtid
            filewrite(cust_data)
            exit()

        case 3:
            phone = input("Please Enter Your New Phone Number: ")
            while len(phone) < 10 or len(phone) >= 11 or int_check(phone) is False:
                print("Invalid Number !")
                phone = input("Please Enter A 10 Digit Phone NUMBER: ")
            print(f"Your New Phone Number {int(phone)} Is Updated Successfully In Our Database !")
            cust_data[ac]["Phone"] = int(phone)
            filewrite(cust_data)
            exit()

        case 4:
            exit()
    exit()


def deposit(ac):
    pin = pin_check(ac)
    ac = int(ac)
    if pin is False:
        print("Wrong Pin !")
        exit()
    cash = input("Enter The Amount To Be Added: ")
    while int_check(cash) is False:
        print("Please Input A Valid Integer Value For 'Deposit'!")
        cash = input("Enter The Ammount To Be Added: ")
    cash = int(cash)
    conf = input(f"Are You Sure You Want To Deposit Rs {cash}/- To You Account ? (y or n): ")
    while not conf in ("y", "n"):
        print("Invalid Option Selected! Please Enter Either y Or n Only...")
        conf = input(f"Are You Sure You Want To Deposit Rs {cash}/- To You Account ? (y or n): ")
    if conf == "n":
        print("Operation Cancelled By User !")
        print("Please Take Your Money Back !")
        print("Thyanku For Banking With Us")
        exit()
    print(f"Deposit Of Rs {cash} Is Successfull !")
    cust_data[ac]["Amount"] += cash
    filewrite(cust_data)
    current = cust_data[ac]["Amount"]
    print(f"Your New Balance Is {current}/- Only")
    exit()


def forgot(ac):
    print("This Feature Will Be Developed In The Future !")


def new_user():
    new_user_input = []
    for i in user_attributes:
        x = input(f"Enter Your {i}: ")
        new_user_input.append(x)
    ac = new_ac()
    n = dict(zip(user_attributes, new_user_input))
    phone = phone_check()
    print("\nYou Will Need To Deposit 2000/- Initially ")
    check = input("Are You Sure You Want To Deposit The Amount (y or n): ")
    while not check in ("y", "n"):
        print("Invalid Entry !")

    if check == "y":
        cust_data[ac] = n
        cust_data[ac]["Phone"] = phone
        cust_data[ac]["Amount"] = 2000
        pin = pin_create()
        cust_data[ac]["Four Digit Pin"] = pin

        with open("custdata.pkl", "wb") as fp:
            pickle.dump(cust_data, fp)
        fp.close()

        z = f"""      Horizon Bank

        Your Details Are Added Successfully.
        Your Account Number Is -> {ac}
        Your Pin Is {cust_data[ac]["Four Digit Pin"]}
        Please Dont Loose Your Account Number And Four Digit Pin.\n"""
        print(z)

    else:
        print("Account Creation Cancelled ! ")
        return 0


def print_state():
    print("Hello World")


def internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


if internet_connection():
    status = "ONLINE"
else:
    status = "OFFLINE"


def existing_user():
    ac = input("Please Enter Your Account Number: ")
    while int_check(ac) is False or not int(ac) in cust_data.keys():
        print("Sorry, The Account Number You Entered Does Not Belong To Any Account In Our Database.")
        ac = input("Please Re-Enter Your Account Number: ")
    text_ex = f"""\nWelcome! {cust_data[int(ac)]["Name"]}
    You Are Currently Working {status}

    Enter 1 To Ckeck Your Balance.
    Enter 2 To Withdraw Amount.
    Enter 3 To Deposit Amount.
    Enter 4 If You Have Forgotten Your Pin
    Enter 5 If You Want To Change Your Personal Details
    Enter 6 To Exit The Program
    Enter 7 To Clear The Database [Emergency] !\n"""
    print(text_ex)
    valid_entries = [1, 2, 3, 4, 5, 6, 7, 8]
    choice = input("Please Enter Your Choice: ")
    while int_check is False or int(choice) not in valid_entries:
        print("Invalid Choice !")
        print("Please Enter A Valid Choice: ")
    choice = int(choice)
    match choice:
        case 1:
            balance = check_balance(ac)
            print(f"Your Current Balance Is {balance}/- Only")
        case 2:
            withdraw(ac)
        case 3:
            deposit(ac)
        case 4:
            forgot()
        case 5:
            change_details(ac)
        case 6:
            exit()
        case 7:
            clear()