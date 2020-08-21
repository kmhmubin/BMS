import csv


def add():
    field = ['Account No', 'Name', 'Date of Birth', 'Address', 'Contact No', 'Gender', 'Opening Date',
             'Opening Balance']
    rows = []
    filename = "db.csv"
    try:
        with open(filename, 'a') as file:
            # creating a csv writer object
            csvwriter = csv.writer(file)
            csvwriter.writerow(field)
            while True:
                acc_no = int(input("Account No: "))
                name = input("Full Name: ")
                dob = input("Date of Birth: ")
                address = input("Address: ")
                cnt_no = int(input("Contact No: "))
                gender = input("Gender: ")
                open_date = input("Opening Date: ")
                open_bln = float(input("Opening Balance: "))
                # writing the data in rows
                csvwriter.writerow([acc_no, name, dob, address, cnt_no, gender, open_date, open_bln])
                info_verify = input("Above all info correct? [y/n]: ")
                if info_verify.lower() == "y":
                    print('Account Create Successful')
                    break
    except FileNotFoundError as err:
        print(err)


if __name__ == '__main__':
    add()
