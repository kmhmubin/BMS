import pickle


def Menu():  # Function to display the menu
    '''
    to know about your screen resolution use the following
    import shutil
    col = shutil.get_terminal_size().col
    print(<string>.center(col))
    '''


print("*" * 140)
print("MAIN MENU".center(140))
print("1. Insert Record/Records".center(140))
print("2. Display Records as per Account Number".center(140))
print("3. Display Records as per Customer Name".center(140))
print("4. Display Records as per Customer Balance".center(140))
print("5. Delete Record".center(140))
print("6. Update Record".center(140))
print("7. Search Record Details as per the account number".center(140))
print("8. Search Record Details as per the Customer Name".center(140))
print("9. Debit/Withdraw from the account".center(140))
print("10. Credit into the account".center(140))
print("11. Exit".center(140))
print("*" * 140)


def SortAcc(F):  # function to arrange records as per ascending order
    of
    Account
    Number


try:
    with open(F, 'rb+') as fil:
        rec = pickle.load(fil)
rec.sort(key=lambda rec: rec[0])
fil.seek(0)
pickle.dump(rec, fil)
except FileNotFoundError:
print(F, "File has no records")


def SortName(F):  # function to arrange records as per ascending order
    of
    Customer
    Name


try:
    with open(F, 'rb+') as fil:
        rec = pickle.load(fil)
rec.sort(key=lambda rec: rec[1])
fil.seek(0)
pickle.dump(rec, fil)
except FileNotFoundError:
print(F, "File has no records")


def SortBal(F):  # function to arrange records as per ascending order
    of
    Customer
    Balance


try:
    with open(F, 'rb+') as fil:
        rec = pickle.load(fil)
rec.sort(key=lambda rec: rec[7])
fil.seek(0)
pickle.dump(rec, fil)
except FileNotFoundError:
print(F, "File has no records")


def Insert(F):
    try:
        fil = open(F, 'ab+')  # will create file if not existing else read


the
records
from the existing

file.
print(fil.tell())
if fil.tell() > 0:
    fil.seek(0)
Rec1 = pickle.load(fil)
else:
Rec1 = []
while True:  # Loop for accepting records
    Acc = int(input("Enter account no"))
Name = input("Enter Name")
Mob = input("Enter Mobile")
email = input("Enter Email")
Add = input("Enter Address")
City = input("Enter City")
Country = input("Enter Country")
Bal = float(input("Enter Balance"))
Rec = [Acc, Name.upper(), Mob, email.upper(), Add.upper(), City.upper(), Country.upp
       er(), Bal]
Rec1.append(Rec)
ch = input("Do you want to enter more records")
if ch == 'N' or ch == 'n':
    break
print(Rec1)
fil.close()
with open(F, 'wb') as fil:  # will open the file for overwriting
    pickle.dump(Rec1, fil)
except ValueError:
print("Invalid values entered")


def Display(F):  # Function to Display the records in the Binary File
    try:
        with open(F, 'rb') as fil:
            print("=" * 140)


F = "%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE
           ADDRESS","CITY","COUNTRY","BALANCE"))
           print("=" * 140)
Rec = pickle.load(fil)
c = len(Rec)
for i in Rec:
    for
j in i:
# print(j,end='\t')
print("%15s" % j, end=' ')
print()
print("*" * 140)
print("Records Read : ", c)
print("*" * 140)except EOFError:
print("=" * 140)
print("Records Read : ", c)
except FileNotFoundError:
print(F, "File Doesn't exist")


def Update(F):  # Function to change the details of a customer
    try:
        with open(F, 'rb+') as fil:
            Rec1 = pickle.load(fil)


found = -1
A = int(input("Enter the accound no whose details to be changed"))
for i in Rec1:
    if i[0] == A:
        found = 0
ch = input("Change Name(Y/N)")
if ch == 'y' or ch == 'Y':
    i[1] = input("Enter Name")
i[1] = i[1].upper()
ch = input("Change Mobile(Y/N)")
if ch == 'y' or ch == 'Y':
    i[2] = input("Enter Mobile")
ch = input("Change Email(Y/N)")
if ch == 'y' or ch == 'Y':
    i[3] = input("Enter email")
i[3] = i[3].upper()
ch = input("Change Address(Y/N)")
if ch == 'y' or ch == 'Y':
    i[4] = input("Enter Address")
i[4] = i[4].upper()
ch = input("Change city(Y/N)")
if ch == 'y' or ch == 'Y': i[5] = input("Enter City")
i[5] = i[5].upper()
ch = input("Change Country(Y/N)")
if ch == 'y' or ch == 'Y':
    i[6] = input("Enter country")
i[6] = i[6].upper()
ch = input("Change Balance(Y/N)")
if ch == 'y' or ch == 'Y':
    i[7] = float(input("Enter Balance"))
if found == -1:
    print("Account details not found")
else:
    fil.seek(0)
pickle.dump(Rec1, fil)
except EOFError:
print("Records Read : ", c)
except FileNotFoundError:
print(F, "File Doesn't exist")


def Delete(F):  # Function to delete the Record from the File, if it
    exists


try:
    with open(F, 'rb+') as fil:
        Rec = pickle.load(fil)
ch = int(input("Enter the accountno to be deleted"))
for i in range(0, len(Rec)):
    if Rec[i][0] == ch:
        print(Rec.pop(i))
print("Record Deleted")
break
else:
print("Record Not found")
fil.seek(0)
pickle.dump(Rec, fil)except FileNotFoundError:
print(F, "File Doesn't exist")
except KeyError:
print("Record Not found")
except IndexError:
print("Record Not found")


def SearchAcc(F):  # Function to Search for the Record from the File with
    respect
    to
    the
    account
    number


try:
    with open(F, 'rb') as fil:
        Rec = pickle.load(fil)
ch = int(input("Enter the accountno to be searched"))
for i in range(0, len(Rec)):
    if Rec[i][0] == ch:
        print("=" * 140)
F = "%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL
           ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
           print("=" * 140)
      for j in Rec[i]:
print('%15s' % j, end=' ')
print()
break
else:
print("Record Not found")
except FileNotFoundError:
print(F, "File Doesn't exist")


def SearchName(F):  # Function to Search for the Record from the File with
    respect
    to
    the
    customer
    name


try:
    with open(F, 'rb') as fil:
        Rec = pickle.load(fil)
ch = input("Enter the Customer Name to be searched")
for i in range(0, len(Rec)):
    if Rec[i][1] == ch.upper():
        print("=" * 140)
    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL
           ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
           print("=" * 140)
      for j in Rec[i]:
print('%15s' % j, end=' ')
print()
break
else:
print("Record Not found")
except FileNotFoundError:
print(F, "File Doesn't exist")


def Debit(F):  # Function to Withdraw the amount by assuring the min balance
    of
    Rs
    5000


try:
    with open(F, 'rb+') as fil:
        Rec = pickle.load(fil)
print("Please Note that the money can only be debited if min
balance
of
Rs
5000
exists
")
acc = int(input("Enter the account no from which the money is to
be
debited
"))
for i in range(0, len(Rec)):
    if
Rec[i][0] == acc:
Amt = float(input("Enter the amount to be withdrawn"))
if Rec[i][7] - Amt >= 5000:
    Rec[i][7] -= Amt
print("Amount Debited")
break
else:
print("There must be min balance of Rs 5000")
break
else:
print("Record Not found")
fil.seek(0)
pickle.dump(Rec, fil)except FileNotFoundError:
print(F, "File Doesn't exist")


def Credit(F):  # Function to Credit the amount into the account
    try:
        with open(F, 'rb+') as fil:
            Rec = pickle.load(fil)


acc = int(input("Enter the account no from which the money is to
be
credited
"))
for i in range(0, len(Rec)):
    if
Rec[i][0] == acc:
Amt = float(input("Enter the amount to be added"))
Rec[i][7] += Amt
print("Amount Credited")
break
else:
print("Record Not found")
fil.seek(0)
pickle.dump(Rec, fil)
except FileNotFoundError:
print(F, "File Doesn't exist")
Fi = "Bank"
while True:
    Menu()
ch = input("Enter your Choice")
if ch == "1":
    Insert(Fi)
elif ch == "2":
    SortAcc(Fi)
Display(Fi)
elif ch == "3":
SortName(Fi)
Display(Fi) elif ch == "4":
SortBal(Fi)
Display(Fi)
elif ch == "5":
Delete(Fi)
elif ch == "6":
Update(Fi)
elif ch == "7":
SearchAcc(Fi)
elif ch == "8":
SearchName(Fi)
elif ch == "9":
Debit(Fi)
elif ch == "10":
Credit(Fi)
elif ch == "11":
print("Exiting...")
break
else:
print("Wrong Choice Entered")
