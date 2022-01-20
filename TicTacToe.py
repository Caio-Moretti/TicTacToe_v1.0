import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter  # letter is x or o

    def getMove(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = int(input(self.letter + '\'s turn. Input move (0-9): '))
            try:
                val = square
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # stops the loop
            except ValueError:
                print('Invalid square. Try again.')

        return val
