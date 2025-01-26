import os
if not os.path.exists("user_info.txt"):
    with open("user_info.txt", "w"):
        pass

print("Hello! Welcome to this simple Registration System \n")
print("Please select an option below:")
print("1. Create account\n2. Login\n3. Delete Account")

userInp = input("--> ")
if userInp == "1":
    username = input("Username: ")
    while True:
        passwd = input("New password: ")
        confirm = input("Confirmation password: ")
        if passwd == confirm:
            print("User created successfully.")
            break
        else:
            print("Both password did not mach. Try again")
            continue
    with open("user_info.txt", "a") as file:
        file.write(f"{username}\n")
        file.write(f"{passwd}\n")

# elif userInp == "2":

elif userInp == "3":
    username = input("Username: ")
    passwd = input("Password: ")
    while True:
        inp = input("Are you sure you want to delete your account (y/n): ")
        inp.strip().lower()
        if inp == "y" or inp == "yes":
            with open("user_info.txt", "r") as file:
                items = file.readlines()
            break
        else:
            print("Your account wasn't deleted!")
            break

else:
    print("Invalid Input!")
