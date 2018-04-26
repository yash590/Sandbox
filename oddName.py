'''Yash Agarwal'''
'''
name = input("Please enter your name: ")

while name!= "" and name != " ":
    for char in range(0,len(name),2):
            print(char)

if name == "" and name == " ":
    print("Invalid Input. Please enter your name again")
    name = input(">")'''

name = input("Please enter your name: ")
if name == '':
    print("Invalid name. Enter your name again")
    name = input("")
else:
    second_letter = name[::2]
    print(second_letter)