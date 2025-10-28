square = lambda x : x**2
print(square(4))

maximum = lambda a, b : a if a>b else b
print(maximum(3,2))

check = lambda x : 'even' if x%2 ==0 else 'odd'
print(check(5))

add = lambda x,y,z : x+y+z
print(add(2,3,4))

mul = add = lambda x,y,z : x*y*z
print(add(2,3,4))

string = lambda s : len(s)
print(string("python"))


last_charcater = lambda s : s[-1]
print(last_charcater("functions")) 

nums = [1,2,3,4,5,6]
even = list(filter(lambda x:x%2 ==0,nums)) 
print(even)

nums1 = [2,4,5,3,6]
squares = list(map(lambda x : x**2,nums1))
print(squares)

data = [(1,2),(3,4),(4,2)]
sort_data = sorted(data,key = lambda x:x[1])
print(sort_data)

nums = [10, 50, 20, 70, 40]
max_num = max(nums, key=lambda x: x)
print(max_num) 

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x + y, nums)
print(product)  

 
employees = [
    {"name": "tej", "salary": 50000},
    {"name": "sai", "salary": 60000},
    {"name": "sri", "salary": 40000}
]


sorted_employees = sorted(employees, key=lambda x: (-x['salary'], x['name']))

print(sorted_employees)

#****************************************************************
from collections import namedtuple
student = namedtuple('student',['name','marks'])

students=[]

choice = 0

while choice != -1:
    name = input("enter the name :")
    marks = int(input("enter the marks :" ))
    students.append(student(name,marks))
    choice = int(input("enter -1 to exit else give 1"))
max_marks = max(students, key=lambda x: x.marks)
print(max_marks)
