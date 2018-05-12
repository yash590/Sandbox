'''Yash Agarwal'''
'''
name = input("Please enter your name: ")

while name!= "" and name != " ":
    for char in range(0,len(name),2):
            print(char)

if name == "" and name == " ":
    print("Invalid Input. Please enter your name again")
    name = input(">")'''

def main():
    name = get_name()
    second_letter = name[::2]
    print(second_letter)


def get_name():
    name = input("Please enter your name: ")
    name = letter_frequency(name)
    return name


def letter_frequency(name):
    is_correct = False
    while is_correct is False:
        if name == '':
            print("Invalid name. Enter your name again")
            name = input("")
        else:
            is_correct = True
    return name


main()