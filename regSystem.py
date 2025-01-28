import os
from getpass import getpass

if not os.path.exists("user_info.txt"):
    with open("user_info.txt", "w") as file:
        pass
def passCheck(passwd):
    alnumFlag = False
    spChrFlag = False
    for i in passwd:
        if i.isalnum():
            if any(i.isnumeric() for i in passwd):
                alnumFlag = True
        else:
            spChrFlag = True
    if alnumFlag == True and spChrFlag == True:
        return True
    else:
        print("The password must contain at least one uppercase letter a number and a special charater.")
        return False

print("Hello! Welcome to this Registration System \n")
while True:
    print("Please select an option below:")
    print("1. Create account\n2. Login\n3. Delete Account\n4. Exit")
    userInp = input("--> ")

# This part is for creating an account
    if userInp == "1":
        uNameChecker = True
        while uNameChecker:
            username = input("Username: ")
            if username.isalnum() and username.islower():
                with open("user_info.txt", "r") as file:
                    if username in file.read():
                        print("This username is taken. Try again.")
                        continue
                uNameChecker = False
            else:
                print("The username can only have lowercase cherecters and numbers.")
        while True:
            passwd = getpass("New password: ")
            if passCheck(passwd) == True:
                confirm = getpass("Confirm password: ")
                if passwd == confirm:
                    print("\nUser created successfully.\n")
                    break
                else:
                    print("Both password did not mach. Try again.")
                    continue

        with open("user_info.txt", "a") as file:
            file.write(f"{username}\n")
            file.write(f"{passwd}\n")

# This part is for log in  
    elif userInp == "2":
        username = input("Username: ")
        passwd = getpass("Password: ")
        with open("user_info.txt", "r") as file:
            if username and passwd in file.read():
                print("\nCongratulations! You have successfully logged in.\n")
            elif username or passwd in file.read():
                print("\nThe username or password is incorrect. Try again.\n")
            else:
                print("\nUser does not exist\n")

# This part is for deleting an account
    elif userInp == "3":
        username = input("Username: ")
        passwd = getpass("Password: ")
        with open("user_info.txt", "r") as file:
            if username and passwd in file.read():
                while True:
                    inp = input("Are you sure you want to delete your account (y/n): ")
                    inp.strip().lower()
                    if inp == "y" or inp == "yes":
                        with open("user_info.txt", "r") as file:
                            items = file.readlines()
                            li = list(items)
                        li.remove(f"{username}\n")
                        li.remove(f"{passwd}\n")
                        with open("user_info.txt", "w") as file:
                            file.write("".join(li))
                        print("\nUser deleted successfully.\n")
                        break
                    elif inp == "n" or inp == "no":
                        print("\nYour account was not deleted.\n")
                        break
                    else:
                        print("Invalid input!")
                        continue
            else:
                print("The username or the password is invalid!")

# this part is for exiting the program
    elif userInp == "4":
        break

    else:
        print("Invalid Input!")
