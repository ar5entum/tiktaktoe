    try:
            move(pos_x, pos_y)
        except:
            print('invalid move')
        if win(pos_x, pos_y):
            print(f'side {side} wins')
            break