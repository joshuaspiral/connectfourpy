from math import inf
ai = "Y"
human = "R"
HEIGHT = 6
WIDTH = 7


def find_best_move(grid):
    best_score = -inf
    best_move = (0, 0)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == " ":  # free space available
                grid[i][j] = ai
                score = minimax(grid, 0, False)
                grid[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def minimax(grid, depth, is_maximising):
    print(depth)
    result = check_for_win(grid)
    if result == ai:
        return 1
    elif result == human:
        return -1
    elif result == "DRAW":
        return 0

    if is_maximising:
        best_score = -inf
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == " ":  # free space available
                    grid[i][j] = ai
                    score = minimax(grid, depth + 1, False)
                    grid[i][j] = " "
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = inf
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == " ":  # free space available
                    grid[i][j] = human
                    score = minimax(grid, depth + 1, False)
                    grid[i][j] = " "
                    if score < best_score:
                        best_score = score
        return best_score


def four_cont_subarray(arr):
    count = 0
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1] and arr[i] != " ":
            count += 1
            if count + 1 >= 4:
                return arr[i]
        else:
            count = 0
    return False


def check_for_win(grid):
    cols = [[row[i] for row in grid] for i in range(WIDTH)]
    for row in grid:
        if four_cont_subarray(row) is not False:
            return four_cont_subarray(row)

    for col in cols:
        if four_cont_subarray(col) is not False:
            return four_cont_subarray(col)

    for row in range(HEIGHT - 3):
        for col in range(3, WIDTH):
            if (
                grid[row][col]
                == grid[row + 1][col - 1]
                == grid[row + 2][col - 2]
                == grid[row + 3][col - 3]
                and grid[row][col] != " "
            ):
                return grid[row][col]

    for row in range(HEIGHT - 3):
        for col in range(WIDTH - 3):
            if (
                grid[row][col]
                == grid[row + 1][col + 1]
                == grid[row + 2][col + 2]
                == grid[row + 3][col + 3]
            ):
                return grid[row][col]

    return False


def handle_turn(player):
    global current_turn
    print_grid(grid)
    col = int(input(f"Which column? From 1-{WIDTH} ")) - 1

    for i in range(HEIGHT - 1, -1, -1):
        if (grid[i][col]) == " ":
            grid[i][col] = player
            break

    result = check_for_win(grid)
    if result == ai:
        return "AI  wins"
    elif result == human:
        return "Human wins"
    elif result == "DRAW":
        return "DRAW"
    else:
        if current_turn == "Y":
            current_turn = "R"
        else:
            current_turn = "Y"


def print_grid(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("|", end=" ")
            print(grid[i][j], end=" ")
        print("|")
    print("-" * 29)
    print(" ", end="")
    print("   ".join([str(x) for x in range(1, WIDTH + 1)]))


grid = [[" " for _ in range(WIDTH)] for x in range(HEIGHT)]
current_turn = human
while True:
    if current_turn == human:
        result = handle_turn(current_turn)
        if result:
            print(result)
            print_grid(grid)
            break
    else:
        y, x = find_best_move(grid)
        grid[y][x] = ai

        result = check_for_win(grid)
        if result == ai:
            print("AI wins")
            break
        elif result == human:
            print("Human wins")
            break
        elif result == "DRAW":
            print("DRAW")
            break
        else:
            if current_turn == "Y":
                current_turn = "R"
            else:
                current_turn = "Y"
