''''n=int(input("enter number:"))
if n==0 or n==1:
    print("not prime")
elif n>1:
    for i in range(2,n):
        if n%2==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")

#this function check the given number is prime or not. return value is bool.
def check_prime(n):
    if n == 0 or n == 1:
        print("not prime")
    elif n > 1:
        for i in range(2,n):
            if n%2==0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")

n = int(input("Enter number to check prime or not:"))

check_prime(n)

def check_prime(n):
    if n == 0 or n == 1:
        return False
    elif n > 1:
        for i in range(2,n):
            if n%2==0:
                print("not prime")
                break
        else:
            return True
    else:
        return False

n = int(input("Enter number is prime or not:"))

print(check_prime(n))

#check the given range of prime numbers
def check_prime(start,end):
    if start <= 1 and end <= 1
        for i in range(start,end+1):
            if i%2==0:
                print(i)
                break
        else:
            print("prime")
    else:
        print("not prime")

start = int(input("Enter number to check prime or not:"))

end=int(input("enter number:"))

check_prime()

# this function gives range of prime numbers

def check_prime(start, end):
    for i in range(start, end + 1):
        if i > 1:  # prime numbers are greater than 1
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end} are:")
check_prime(start, end) # calling the function

#this function gives list of squares of only odd numbers

def list_of_square_of_odd_numbers(start, end):
    squares_list = []  # list to store squares of odd numbers
    for i in range(start, end):
        if i % 2 != 0:  
            squares = i ** 2
            squares_list.append(squares)
    return squares_list

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

print("Squares of odd numbers are:", list_of_square_of_odd_numbers(start, end))




# this function  find how many vowels in a string
def vowels_count(string):
    vowels="AEIOUaeiou"
    count=0
    for i in string:
        if i in vowels:
            count += 1
    print(count)

string = input("Enter the string:")
vowels_count(string)

# this function finds factors of the numbers

def find_factors(number):
    print(f"Factors of {number} are:")
    for i in range(1, number + 1): 
        if number % i == 0:
            print(i)

number = int(input("Enter the number: "))
find_factors(number)


# this program finds only the names that start with a vowel into a
new list.

name_list = ["Teja","anshu","radha","usha","sri"]
vowels = "AEIOUaeiou"
new_list = []

for i in name_list:
    if i[0] in vowels:
        new_list.append(i)

print(new_list)

i = 1
number=int(input("Enter the number"))
while i < number:
  print(i)
  i += 1 

#
while True:
    num = int(input("Enter a positive number : "))
    if num < 0:
        print("Negative number entered and Stopping the loop.")
        break
    else:
        print(f"You entered: {num}")'''





    



