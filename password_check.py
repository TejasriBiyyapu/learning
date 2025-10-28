# 17. Write a Python program that asks for a password and grants access only if the password matches and the user has not exceeded 3 failed attempts (use while loop and logical operators).

original_password = "Teja123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == original_password:
        print("Access Granted ")
        break
    else:
        attempts += 1
        print("Wrong password ")

if attempts == 3:
    print("Access Denied ")




