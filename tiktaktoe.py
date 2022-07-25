arr = [['_', '_', '_'], ['_', '_', '_'], [' ', ' ', ' ']]

side = 'x'

move_count = 0


def display():
    for i in arr:
        print(*i, sep='|')
    print()


def move(pos_x, pos_y):

    global side
    global move_count
    if arr[pos_x][pos_y] not in ['x', 'o']:
        try:
            arr[pos_x][pos_y] = side
            display()
            if win():
                print(f'side {side} wins')

        except:
            print('invalid move')

        if side == 'x':
            side = 'o'
        else:
            side = 'x'
        move_count += 1
    else:
        print('invalid move')


def win():
    wins = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    for i in wins:
        if arr[i[0][0]][i[0][1]] == side and arr[i[1][0]][i[1][1]] == side and arr[i[2][0]][i[2][1]] == side:
            return True
        else:
            return False


while move_count != 9:
    pos = input()
    pos_x = ord(pos[0].lower()) - 97
    pos_y = int(pos[1]) - 1
    move(pos_x, pos_y)
    pass
