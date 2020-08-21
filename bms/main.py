import datetime
import os
import sys
import time
import csv


def welcome():
    print("-" * 80)
    print("\t\tBank Management System")
    print("\t\tCreate by Mubin")
    print("-" * 80)


def screen_clear():
    """
    terminal screen clear
    :return:
    """
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def main():
    # welcome screen
    welcome()
    # wait 2 seconds
    time.sleep(2)
    print("Press any key to continue")
    input()

    while True:
        # clear screen
        screen_clear()
        print("Press A to Login as Admin or C to Login as Customer")
        enter = input("Enter: ")
        if enter == 'A' or enter == 'a':
            admin()
            break
        elif enter == "C" or enter == 'c':
            print("Customer")
            break
        else:
            print("Invalid Option")
            sys.exit(0)


def admin():
    """ Admin function """
    num_attempts = 0
    user = {"ADMIN": "PASSWORD"}

    while num_attempts < 3:
        # system('clear')
        screen_clear()
        print(f"3 out of {num_attempts}")
        username = input("Username: ").upper()
        password = input("Password: ").upper()
        if username in user and password == user[username]:
            print("Access Granted")
            time.sleep(1)
            break
        else:
            print("Wrong Info. Try again")
            num_attempts += 1

    ch = ""
    while ch != 5:
        screen_clear()
        title(username)
        print("\t 1. Open Account")
        print("\t 2. Edit Account")
        print("\t 3. Delete Account")
        print("\t 4. View Accounts")
        print("\t 5. exit")
        print("-" * 80)
        ch = input("Select An Option (1-5): ")
        print("-" * 80)

        if ch == '1':
            open_account(username)
        elif ch == '2':
            print("Edit account")
            break
        elif ch == '3':
            print("Delete account")
            break
        elif ch == '4':
            print("View account")
            break
        elif ch == '5':
            print("Are you sure you want to exit? <Y/N>: ")
            ex = input()
            if ex == "Y" or ex == "y":
                exit(0)
                print(" Thanks for using this service")
                break
        else:
            print("Invalid Choice")
            break


def title(username):
    screen_clear()
    # showing current date and time
    today = datetime.datetime.now()
    dt = today.strftime("%a, %b %d, %Y")
    tm = today.strftime("%I:%M:%S %p")
    print("-" * 80)
    print("\t\t\t Bank Management System ")
    print("-" * 80)
    print(f"Current User: {username} | Date: {dt} | Time: {tm}")
    print("-" * 80)


def open_account(username):
    screen_clear()
    title(username)

    field = ['Account No', 'Name', 'Date of Birth', 'Address', 'Contact No', 'Gender', 'Opening Date',
             'Opening Balance']
    # rows = []
    open_bln = 0.0
    filename = "db.csv"
    try:
        with open(filename, 'a') as file:
            # creating a csv writer object
            csvwriter = csv.writer(file)
            csvwriter.writerow(field)
            while True:
                acc_no = int(input("Account No: "))
                name = input("Full Name: ").capitalize()
                dob = input("Date of Birth [dd/mm/yyyy]: ")
                address = input("Address: ").capitalize()
                cnt_no = int(input("Contact No: "))
                gender = input("Gender[m/f]: ").capitalize()
                open_date = datetime.date
                open_bln = float(input("Opening Balance: "))
                # writing the data in rows
                csvwriter.writerow([acc_no, name, dob, address, cnt_no, gender, open_date, open_bln])
                info_verify = input("Above all info correct? [y/n]: ")
                if info_verify.lower() == "y":
                    print('Account Create Successful')
                    time.sleep(1)
                    break
    except FileNotFoundError as err:
        print(err)


if __name__ == '__main__':
    main()
