#this function helps to check give number is palindrom or not

def check_palindrome(original_number):
    number = original_number
    reverse_number = 0

    # reverse the entire number using while loop
    while number > 0:
        digit = number % 10          # get last digit
        reverse_number = reverse_number * 10 + digit  # build reversed number
        number = number // 10        # remove last digit

    if reverse_number == original_number:
        return True
    else:
        return False


original_number = int(input("Enter the number: "))
print(check_palindrome(original_number))