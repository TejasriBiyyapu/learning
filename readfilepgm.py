# Step 1: Read and show current content
with open('test.txt', 'r') as f:
    print("Current content:\n", f.read())

# Step 2: Take input and append to file
n = input("Enter text to add: ")
with open('test.txt', 'a') as f:
    f.write(n + "\n")  # Add a newline

# Step 3: Read and show updated content
with open('test.txt', 'r') as f:
    print("\nUpdated content:\n", f.read())



