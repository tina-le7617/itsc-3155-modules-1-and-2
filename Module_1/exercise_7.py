array = []
even_num = []

while True:
    choice = input('Enter a number or QUIT to quit: ')
    if choice.upper() != 'QUIT':
        array.append(int(choice))
    else:
        for i in range(len(array)):
            if (array[i] % 2) == 0:
                even_num.append(array[i])
        print(even_num)
        break