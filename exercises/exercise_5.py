first_list = []

for index in range(5):
    first_numbers = int(input(f'Enter a number for the first list: '))
    first_list.append(first_numbers)

second_list = []

for index in range(5):
    second_numbers = int(input(f'Enter a number for the second list: '))
    second_list.append(second_numbers)

third_list = []

for index in range(len(first_list)):
    if first_list[index] in second_list:
        third_list.append(first_list[index])

print(third_list)