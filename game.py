class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to rep 3x3 board
        self.current_winner = None  # keep track of the winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def num_empty_squares(self):
        return self.board.count(' ')

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these!
        # firs let's check the row
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game! or None for a tie

    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():

        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
        if print_game:
            print('It\'s a tie.')


game = TicTacToe()
game.print_board()

#  53:01
