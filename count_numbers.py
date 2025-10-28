# 20. Write a program that continuously reads integers from the user and writes them into a file until the user types “STOP”;then print the total count of even and odd numbers written.
even_count = 0
odd_count = 0

with open("numbers.txt", "w") as file:
    while True:
        user_input = input("Enter a number (or type STOP to end): ")

        if user_input.upper() == "STOP":
            break

        data = int(user_input)
        file.write(str(data) + "\n")

        if data % 2 == 0:
            even_count += 1
        else:
            odd_count += 1


print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
