file = open("test.txt",'r')
lines = file.readlines()
for i in lines:
    if 'python' in i:
        print(i)

