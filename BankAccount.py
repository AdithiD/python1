import re

search1=[]
search2=[]
search3=[]
search4=[]
print("ABC BANK FORM")
print("Please fill in up the details ")
accountexistance = input("Do you have an account in this bank (yes/no) : ")
if accountexistance.isdigit() :
    print("It seems like you entered a number instead of yes or no So please try again!!")
elif accountexistance.lower() == "yes" or accountexistance.lower() == "y":
    print("Ok, please fill in the details to verify!!")
    with open("AccountDetails.txt" , "r")as file:
        read = file.read()
        name = input("Enter full name : ")
        accountnum = input("Enter account number : ")
        mobilenum = input("Enter Registered Mobile Number : +91")
        validAN = r"\d{8,12}"
        validMN = r"\d{10}"
        balance = r'\₹([0-9,]+\.\d{2})'
        validname = r"\w[A-Za-z]"
        search1 = re.findall(validAN , read)
        search2 = re.findall(validMN, read)
        search4 = re.findall(validname , read)
for i in range (0,len(search1),1):    
    if accountnum == search1[i] and mobilenum == search2[i] and name == search4[i]:
        print("Name : " , search4)
        print("Account Number : ",search1)
        print("Mobile Number : +91",search2)
        print("Balance :₹ ",search3)
    else:
        print("Invalid Input")


