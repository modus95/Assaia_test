'''Connect 4 game'''

def printfield(field):
    '''Prints game's field'''

    rows = ['a','b','c','d','e','f']
    bottom_line = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-'*(len(bottom_line)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(field[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(bottom_line)
    print('')


def step(player, field, columns):
    '''A player's step'''

    input_set = [str(i) for i in range(1,8)]
    symb = 'X' if player == 'Player_1' else 'O'

    pos_col = str(input(player + ': '))
    if not pos_col in input_set:
        print('Please enter digits [1..7]')
        step(player, field, columns)
    else:
        pos_col = int(pos_col)
        if len(columns[pos_col-1]) < 6:
            columns[pos_col-1].append(symb)
            pos_col_ln = len(columns[pos_col-1])
            field[6 - pos_col_ln][pos_col-1] = columns[pos_col-1][-1]
        else:
            print('This column is full, try another column..')
            step(player, field, columns)

    return field, columns


def check_end(player ,field):
    '''Check end of the game (win)'''
    game_fl = False
    symb = 'X' if player == 'Player_1' else 'O'

    # Horiz check
    for j in range(0,6):
        for i in range(3,7):
            if field[j][i]==field[j][i-1]==field[j][i-2]==field[j][i-3]==symb:
                game_fl = True
                break

    # Vert chek
    for i in range(0,7):
        for j in range(3,6):
            if field[j][i]==field[j-1][i]==field[j-2][i]==field[j-3][i]==symb:
                game_fl = True
                break

    # Diag check
    for i in range(0,4):
        for j in range(0,3):
            if (field[j][i]==field[j+1][i+1]==field[j+2][i+2]==field[j+3][i+3]==symb) or \
                (field[j+3][i]==field[j+2][i+1]==field[j+1][i+2]==field[j][i+3]==symb):
                game_fl = True
                break

    if game_fl:
        print(player + ' wins')
    return game_fl


def main():
    '''Main program'''

    field = []
    for _ in range(6):
        field.append([' '] * 7)

    columns = {c:[] for c in range(7)}

    printfield(field)
    print('Please enter digits [1..7]')

    end_game_fl = False
    while not end_game_fl:
        # Player 1
        field, columns = step('Player_1', field, columns)
        printfield(field)
        end_game_fl = check_end('Player_1',field)
        if end_game_fl:
            break

        # Player_2
        field, columns = step('Player_2',field, columns)
        printfield(field)
        end_game_fl = check_end('Player_2',field)

    print('End of game!')


if __name__ == '__main__':
    main()
