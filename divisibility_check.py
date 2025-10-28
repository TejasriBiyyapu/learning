# 16. Create a program that prints numbers between 1 and 100 that are divisible by either 3 or 5 but not both.
def divisible_numbers(start,end):
    for i in range(start, end+1):
        if ( i % 3 == 0 or i % 5 == 0 ) and not (i % 3 == 0 and i % 5 == 0 ):
            print(i)

start = int(input("Enter the range start number :"))
end = int(input("Enter the range end number :"))
divisible_numbers(start,end)
