# Create a program that counts how many lines, words, and characters exist in a text file.

f = open("test.txt", 'r')

lines = f.readlines()

word_count = 0
char_count = 0

for i in lines:
    word_count += len(i.split())    
    char_count += len(i) 


print("The number of lines in the file:", len(lines))
print("The number of words in the file:", word_count)
print("The number of characters in the file:", char_count)

f.close()
