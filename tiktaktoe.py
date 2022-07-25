arr = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    [' ', ' ', ' ']
]

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
        arr[pos_x][pos_y] = side
        display()

        if side == 'x':
            side = 'o'
        else:
            side = 'x'
        move_count += 1
    else:
        print('invalid move')


def win(x, y):
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
        if arr[i[0][0]][i[0][1]] == arr[i[1][0]][i[1][1]] == arr[i[2][0]][i[2][1]] == 'x' or arr[i[0][0]][i[0][1]] == arr[i[1][0]][i[1][1]] == arr[i[2][0]][i[2][1]] == 'y':
            return True
    return False


display()

while True:
    pos = input() 
    if len(pos) != 2:
        continue
    pos_x = ord(pos[0].lower()) - 97
    pos_y = int(pos[1]) - 1
    try:
        move(pos_x, pos_y)
        if win(pos_x, pos_y):
            print(f'side {side} wins')
            break
        elif move_count == 9:
            print('its a tie')
            break
    except:
        print('invalid move')
exit()
