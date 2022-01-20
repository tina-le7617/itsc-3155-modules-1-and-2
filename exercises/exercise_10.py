result = []
arr = []

string = input('Enter a string: ')

for i in range(len(string)):
    if i % 3 == 0 and i != 0:
        result.append(arr)
        arr = []
    arr.append(string[i])

result.append(arr)

print(result)