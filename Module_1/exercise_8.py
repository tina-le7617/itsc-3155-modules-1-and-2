list = []
temp_list = []

for i in range(10):
    integers = int(input('Enter a number: '))
    temp_list.append(integers)

for i in temp_list:
    if temp_list[i] not in list:
        list.append(temp_list[i])
    else:
        list.remove(temp_list[i])

print(list)