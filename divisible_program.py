# 13. Write a Python program that checks if a number is divisible by both 3 and 5, but not by 7.

def divisible_check (number):
    if ( number % 5 == 0 and number % 3 == 0 ) and number % 7 != 0:
        return True
    else:
        return False

number = int(input("Enter the number :"))
print(divisible_check (number))