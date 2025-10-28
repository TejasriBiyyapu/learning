# 18. Using nested if-else, write a program that classifies a triangle as equilateral, isosceles, or scalene based on user input sides

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a == b == c:
    print("Equilateral Triangle")
else:
    if a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
