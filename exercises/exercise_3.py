integer = int(input('Enter an integer greater than 1: '))

for index in range(integer + 1):
    print(f'The square of {index} is {pow(index, 2)} ')