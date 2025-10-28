#14. Using logical operators, write a program that accepts a user’s age and salary and determines if they are eligible for a loan (age ≥ 21 and salary ≥ ₹25,000).

def loan_eligibility (age,salary): #
    if age >= 21 and salary >= 27000:
        print("Eligible for loan")

    else:
        print("Not eligible for loan")


age = int(input("Enter the age :"))
salary = int(input("Enter the salary :"))
loan_eligibility (age,salary)

