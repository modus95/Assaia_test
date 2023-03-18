'''Connect 4 game'''
import argparse

class Field():
    "Game's field"
    def __init__(self, q_rows: int, q_cols: int) -> None:
        self.q_rows = q_rows
        self.q_cols = q_cols

        self.map = []
        for _ in range(self.q_rows):
            self.map.append([' '] * self.q_cols)

        self.columns = {c:[] for c in range(self.q_cols)}


    def printfield(self) -> None:
        '''Prints game's field'''
        bottom_line = ''
        for c in range(1, self.q_cols + 1):
            bottom_line += f'{c}   '
        bottom_line = '  ' + bottom_line

        print('')
        print(' ' + '-' * (len(bottom_line) - 3))
        for row in range(self.q_rows):
            print('| ' + ' | '.join(self.map[row]) + ' |')
            print(' ' + '-' * (len(bottom_line) - 3))
        print(bottom_line)
        print()

    
    def check_end(self, ind_row:int, ind_col:int) -> bool:
        '''Check end of the game (win)'''
        
        symb = self.map[ind_row][ind_col]
        symb_4 = symb * 4

        # Horiz check
        game_fl = symb_4 in ''.join(self.map[ind_row])
        if game_fl:
            return game_fl

        # Vert chek
        game_fl = symb_4 in ''.join(self.columns[ind_col])
        if game_fl:
            return game_fl

        #Diag check
        diag_upleft = []
        for i in range(1, 4):
            cur_col = ind_col - i
            cur_row = ind_row - i
            if (cur_col < 0) or (cur_row < 0):
                break
            diag_upleft.append(self.map[cur_row][cur_col])

        diag_downleft = []
        for i in range(1, 4):
            cur_col = ind_col - i
            cur_row = ind_row + i
            if (cur_col < 0) or (cur_row > self.q_rows - 1):
                break
            diag_downleft.append(self.map[cur_row][cur_col])

        diag_upright = []
        for i in range(1, 4):
            cur_col = ind_col + i
            cur_row = ind_row - i
            if (cur_col > self.q_cols - 1) or (cur_row < 0):
                break
            diag_upright.append(self.map[cur_row][cur_col])

        diag_downright = []
        for i in range(1, 4):
            cur_col = ind_col + i
            cur_row = ind_row + i
            if (cur_col > self.q_cols - 1) or (cur_row > self.q_rows - 1):
                break
            diag_downright.append(self.map[cur_row][cur_col])

        diag1 = diag_upleft[::-1] + [symb] + diag_downright
        diag2 = diag_downleft[::-1] + [symb] + diag_upright

        game_fl = (symb_4 in ''.join(diag1)) or (symb_4 in ''.join(diag2))
        return game_fl


    def step(self, id_player:int) -> bool:
        '''A player's step'''

        #input_set = [str(i) for i in range(1, self.q_cols + 1)]
        symb = 'X' if id_player == 0 else 'O'

        pos_col = int(input(f'Player_{id_player + 1}: '))
        if 1 <= pos_col <= self.q_cols:
            ind_col = pos_col - 1
            if len(self.columns[ind_col]) < self.q_rows:
                self.columns[ind_col].append(symb)
                pos_col_ln = len(self.columns[ind_col])
                ind_row = self.q_rows - pos_col_ln
                self.map[ind_row][ind_col] = symb
            else:
                print('This column is full, try another column..')
                self.step(id_player)
        else:
            print(f'Please enter digits [1..{self.q_cols}]')
            self.step(id_player)

        game_fl = self.check_end(ind_row, ind_col)
        
        return game_fl


def run(q_rows, q_cols):
    '''Main program'''

    field = Field(q_rows, q_cols)

    field.printfield()
    print(f'Please enter numbers [1..{q_cols}]')

    end_game_fl = False
    max_steps = q_rows * q_cols
    cur_step = 0

    while not end_game_fl:
        id_gamer = cur_step % 2
        end_game_fl = field.step(id_gamer)
        field.printfield()
        cur_step += 1

        if end_game_fl:
            print(f'Player_{id_gamer + 1} has won!')
        elif cur_step == max_steps:
            print("It's a draw! Nobody wins.")
            end_game_fl = True

    print('End of the game!')

if __name__ == '__main__':
    DESC = 'Connect4 game'

    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('-r', '--q_rows', type=int, default=6, help="int (default: %(default)s)")
    parser.add_argument('-c', '--q_cols', type=int, default=7, help="int (default: %(default)s)")
    args = parser.parse_args()

    run(args.q_rows, args.q_cols)
    