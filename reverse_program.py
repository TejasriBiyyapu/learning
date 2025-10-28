#reverse the number using while loop
num = int(input("Enter an integer to reverse: "))
reversed_num = 0

while num != 0:
    digit = num % 10          # get the last digit
    reversed_num = reversed_num * 10 + digit  
    num = num // 10           # remove last digit

print(f"The reverse of  is {reversed_num}") 
