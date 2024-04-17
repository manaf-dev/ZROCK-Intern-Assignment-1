# Program to check if a number is positive, negative or zero

def check_number(num):
    if num > 0:
        print(f'{num} is a positive number.')
    elif num < 0:
        print(f'{num} is a negative number.')
    else:
        print(f'{num} is zero.')


number = int(input('Enter a number: '))
check_number(number)