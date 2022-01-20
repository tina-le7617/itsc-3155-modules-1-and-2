# https://stackoverflow.com/questions/24023115/how-to-initialise-a-2d-array-in-python

row, col = 5, 5
grid = []

row_num = int(input(f'Enter a row num from 1 to 5: '))
col_num = int(input(f'Enter a col num from 1 to 5: '))

for i in range(row):
    grid.append([])
    for j in range(col):
        grid[i].append(0)

grid[row_num - 1][col_num - 1] = 1

for i in range(row):
    for j in range(col):
        print(f'{grid[i][j]}', end = " ")
    print('')