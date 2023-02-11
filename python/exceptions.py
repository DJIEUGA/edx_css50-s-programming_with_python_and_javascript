import sys
print('Hello from exceptions.py')


try:
    x = int(input('Enter a number: '))
    y = int(input('Enter a another number: '))
except ValueError:
    print('Input Error')
    # exit program
    sys.exit(1)

try:
    results = x / y
except ZeroDivisionError:
    print('Error: Cannot divide by 0!')
    # Exit the program
    sys.exit(1)

print(f'{x} / {y} = {results}')
