# 12. Write a script to copy the contents of one text file into another, but exclude all lines that start with a “#” symbol.e

file = open("test.txt", 'r')

destination = open("test.txt", 'w')

for i in file:
    line = i.strip()   
    
    if len(line) > 0 and line[0] != '#':
        destination.write(line + '\n')

file.close()
destination.close()

print("File copied successfully")


