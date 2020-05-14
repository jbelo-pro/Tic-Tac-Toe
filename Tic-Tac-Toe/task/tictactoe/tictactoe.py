
def create_matrix(text):
    m = []
    for p in range(3, 10, 3):
        m.append([x for x in text[p - 3: p]])
    return m


def horizontal(symbol, matrix):
    winner = False
    for row in matrix:
        win = True
        for cell in row:
            if cell != symbol:
                win = False
                break
        if win:
            winner = True
            break
    return winner


def vertical(symbol, matrix):
    t_matrix = [[y for y in  x] for x in zip(*matrix)]
    return horizontal(symbol, t_matrix)


def diagonal(symbol, matrix):
    winner = True
    for i in range(3):
        if matrix[i][i] != symbol:
            winner = False
    if winner:
        return winner
    winner = True
    for i in range(3):
        if matrix[i][-(i + 1)] != symbol:
            winner = False
    return winner


def is_winner(symbol, matrix):
    if vertical(symbol, matrix) or \
       horizontal(symbol, matrix) or \
       diagonal(symbol, matrix):
        return True
    else:
        return False


def invalid_symbols(matrix):
    symbo_x = 0
    symbo_y = 0

    for row in matrix:
        for c in row:
            if c == 'X':
                symbo_x += 1
            elif c == 'O':
                symbo_y += 1
    if abs(symbo_y - symbo_x) >= 2:
        return True
    else:
        return False


def is_impossible(matrix):
    if is_winner('X', matrix) and is_winner('O', matrix) or invalid_symbols(matrix):
        return True
    else:
        return False


def has_space(matrix):
    counter = 0
    for row in matrix:
        for c in row:
            if c == '_':
                counter += 1
    if counter:
        return True
    else:
        return False


def print_matrix(matrix):
    print('---------')
    for row in matrix:
        line = '| {} {} {} |'.format(row[0], row[1], row[2])
        print(line)
    print('---------')


def convert_coordinates(a_coor, b_coor):
    row = 2 - (b_coor - 1)
    pos = a_coor - 1
    return row, pos


def coor_is_number(coor):
    if len(coor) != 2 or not coor[0].isnumeric() or not coor[1].isnumeric():
        return False
    else:
        return True


def coor_in_range(coor):
    if coor[0] not in ['1', '2', '3'] or coor[1] not in ['1', '2', '3']:
        return False
    else:
        return True


def check_available_coor(matrix, row, pos):
    if matrix[row][pos] == 'X' or matrix[row][pos] == 'O':
        return False
    else:
        return True


matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print_matrix(matrix)
player = 'X'
while True:
    if is_winner('X', matrix):
        print('X wins')
        break
    elif is_winner('O', matrix):
        print('O wins')
        break
    elif not has_space(matrix):
        print('Draw')
        break
    else:
        position = input('Enter the coordinates: ').split()
        if not coor_is_number(position):
            print('You should enter numbers!')
            continue
        if not coor_in_range(position):
            print("Coordinates should be from 1 to 3!")
            continue
        row, pos = convert_coordinates(int(position[0]), int(position[1]))
        if not check_available_coor(matrix, row, pos):
            print("This cell is occupied! Choose another one!")
        else:
            matrix[row][pos] = player
            player = 'X' if player == 'O' else 'O'
            print_matrix(matrix)

