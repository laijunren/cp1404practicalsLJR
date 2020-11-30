def main():
    print('1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius')
    choice = input('> ')
    while True:
        if choice == '1':
            fahrenheit = C_F()
            print('fahrenheit is', fahrenheit, '\n')
        elif choice == '2':
            celsius = F_C()
            print('celsius is', celsius, '\n')
        else:
            print('Invalid choice\n')
        print('1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius')
        choice = input('> ')


def C_F():
    celsius = float(input('Enter celsius: '))
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def F_C():
    fahrenheit = float(input('Enter fahrenheit: '))
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


main()
