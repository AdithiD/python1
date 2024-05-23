
import re

print("ABC BANK FORM")
print("Please fill in up the details ")
accountexistance = input("Do you have an account in this bank (yes/no) : ")
if accountexistance.isdigit() :
    print("It seems like you entered a number instead of yes or no So please try again!!")
elif accountexistance.lower() == "yes" or accountexistance.lower() == "y":
    print("Ok, please fill in the details to verify!!")
    with open("Accountdetails.txt" , "r")as file:
        read = file.read()
        name = input("Enter full name : ")
        accountnum = input("Enter account number : ")
        mobilenum = input("Enter Registered Mobile Number : +91")
        validAN = r"\d{8,12}"
        validMN = r"\d{10}"
        balance = r'\₹([0-9,]+\.\d{2})'
        search1 = re.findall(validAN , accountnum)
        search2 = re.findall(validMN, mobilenum)
        search3 = re.findall(balance , read)
        if search1  and search2 and search3:
            print("Name : " , name)
            print("Account Number : ",accountnum)
            print("Mobile Number : +91",mobilenum)
            print("Balance :₹ ",search3[0])
        else:
            print("Invalid Input")

