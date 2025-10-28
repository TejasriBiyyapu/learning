#19. Write a script that opens a file named data.txt, reads its numbers, and prints the sum of only even numbers found in the file.

file = open("data.txt",'r')
numbers = file.read().split()

even_sum = 0
for num in numbers:
    n = int(num)
    if n % 2 == 0:
        even_sum += n

print("Sum of even numbers:", even_sum)