#task1
'''
try:
    file=open('sample.txt','r')
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print('File not found')
'''

#task2
text = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")

more_text = input("Enter more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(more_text + "\n")

print("\nFinal content of the file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

