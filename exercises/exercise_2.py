from sys import prefix

first_string = input('Enter a string: ')
second_string = input('Enter another string: ')

if second_string.startswith(first_string):
    print('True')
else:
    print('False')