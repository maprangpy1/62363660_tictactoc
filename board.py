""" A repressentation of a board for the tic-tac-toe game. """

""" Worachot Wongkhuea 62365541"""

class TicTacToeBoard :
    def __init__(self):
        self.board = ["."]*9

    def mark(self, symbol, position):
        self.board[position - 1] = symbol

    def terminate(self):
        
        if (self.board[0] == 'X') and \
            (self.board[1] == 'X') and \
            (self.board[2] == 'X'):
                return 'x012'
        elif (self.board[3] == 'X') and \
            (self.board[4] == 'X') and \
            (self.board[5] == 'X'):
                return 'x345'
        elif (self.board[6] == 'X') and \
            (self.board[7] == 'X') and \
            (self.board[8] == 'X'):
                return 'x678'
        elif (self.board[0] == 'X') and \
            (self.board[3] == 'X') and \
            (self.board[6] == 'X'):
                return 'x036'
        elif (self.board[1] == 'X') and \
            (self.board[4] == 'X') and \
            (self.board[7] == 'X'):
                return 'x147'
        elif (self.board[2] == 'X') and \
            (self.board[5] == 'X') and \
            (self.board[8] == 'X'):
                return 'x258'
        elif (self.board[2] == 'X') and \
            (self.board[4] == 'X') and \
            (self.board[6] == 'X'):
                return 'x246'
        elif (self.board[0] == 'X') and \
            (self.board[4] == 'X') and \
            (self.board[8] == 'X'):
                return 'x048'

        elif (self.board[0] == 'O') and \
            (self.board[1] == 'O') and \
            (self.board[2] == 'O'):
                return 'o012'
        elif (self.board[3] == 'O') and \
            (self.board[4] == 'O') and \
            (self.board[5] == 'O'):
                return 'o345'
        elif (self.board[6] == 'O') and \
            (self.board[7] == 'O') and \
            (self.board[8] == 'O'):
                return 'o678'
        elif (self.board[0] == 'O') and \
            (self.board[3] == 'O') and \
            (self.board[6] == 'O'):
                return 'o036'
        elif (self.board[1] == 'O') and \
            (self.board[4] == 'O') and \
            (self.board[7] == 'O'):
                return 'o147'
        elif (self.board[2] == 'O') and \
            (self.board[5] == 'O') and \
            (self.board[8] == 'O'):
                return 'o258'
        elif (self.board[2] == 'O') and \
            (self.board[4] == 'O') and \
            (self.board[6] == 'O'):
                return 'o246'
        elif (self.board[0] == 'O') and \
            (self.board[4] == 'O') and \
            (self.board[8] == 'O'):
                return 'o048'

    def winner(self):
        if self.terminate() == 'x012' or self.terminate() == 'o012':
            return self.board[0]
        elif self.terminate() == 'x345' or self.terminate() == 'o345':
            return self.board[3]
        elif self.terminate() == 'x678' or self.terminate() == 'o678':
            return self.board[6]
        elif self.terminate() == 'x036' or self.terminate() == 'o036':
            return self.board[0]
        elif self.terminate() == 'x147' or self.terminate() == 'o147':
            return self.board[1]
        elif self.terminate() == 'x258' or self.terminate() == 'o258':
            return self.board[2]
        elif self.terminate() == 'x246' or self.terminate() == 'o246':
            return self.board[4]
        elif self.terminate() == 'x048' or self.terminate() == 'o048':
            return self.board[4]
        return 'Draw!!!'
    