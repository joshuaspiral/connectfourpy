HEIGHT = 6
WIDTH = 7

def four_cont_subarray(arr):
    count = 0
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1] and  arr[i] != ' ':
            count += 1
            if count + 1 >= 4:
                return arr[i]
        else:
            count = 0
    return False

def check_for_win(grid):
    print('checking for win')
    cols = [[row[i] for row in grid] for i in range(WIDTH)]
    for row in grid:
        print(row)
        if four_cont_subarray(row) is not False:
            return four_cont_subarray(row)

    for col in cols:
        if four_cont_subarray(col) is not False:
            return four_cont_subarray(col)

#     for row in range(HEIGHT - 3):
#         for col in range(WIDTH - 3):
#             if grid[row][col] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
#                 return grid[row][col]

#     for row in range(3, HEIGHT):
#         for col in range(WIDTH - 3):
#             if grid[row][col] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
#                 return grid[row][col]

    return False
  

def handle_turn(player):
    global current_turn
    print_grid(grid)
    col = int(input(f"Which column? From 1-{WIDTH} ")) - 1

    for i in range(HEIGHT - 1, -1, -1):
        if (grid[i][col]) == ' ':
            grid[i][col] = player
            break

    result = check_for_win(grid)
    if result == 'Y':
        return 'Yellow wins'
    elif result == 'R':
        return 'Red wins'
    elif result == 'DRAW':
        return 'DRAW'
    else:
        if current_turn == 'Y':
            current_turn = 'R'
        else:
            current_turn = 'Y'

def print_grid(grid):
    print()
    for row in grid:
        for col in row:
            print('|', end=' ')
            print(col, end=' ') 
        print('|')
    print('-'*29)

grid = [[' ' for _ in range(WIDTH)] for x in range(HEIGHT)]
current_turn = 'Y'
while True:
    result = handle_turn(current_turn)
    if result:
        print(result)
        print_grid(grid)
        break
