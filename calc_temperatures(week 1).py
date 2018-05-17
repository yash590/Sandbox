def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temp = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(temp))
        elif choice == "F":
            temp = fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(temp))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius():
    farenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (farenheit - 32)
    return celsius


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
