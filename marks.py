# 15. Write a Python script that reads a list of marks and prints “Pass” if all marks are above 40, otherwise “Fail”, using logical AND.

def marks (marks_list):
    for i in marks_list:
        if i < 40:
            print("Fail")
            break
    else:
        print("Pass")

marks_list = [40,56,78,98]
marks (marks_list)
