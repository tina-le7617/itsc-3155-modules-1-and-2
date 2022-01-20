import sys
import statistics

number = int(input('Enter a number: '))

user_list = []

for index in range(number):
    user_number = float(input(f'Enter number {index + 1}: '))
    user_list.append(user_number)

# https://careerkarma.com/blog/python-average/
average = statistics.mean(user_list)

print(f'List: {user_list}')
print(f'Average: {average}')