from board import TicTacToeBoard
def test_O_row1():
    board = TicTacToeBoard()

    board.mark("O", 1)
    board.mark("O", 2)
    board.mark("O", 3)

    assert board.winner() == "O"

def test_X_row1():
    board = TicTacToeBoard()

    board.mark("X", 1)
    board.mark("X", 2)
    board.mark("X", 3)

    assert board.winner() == "X"

def test_O_row2():
    board = TicTacToeBoard()

    board.mark("O", 4)
    board.mark("O", 5)
    board.mark("O", 6)

    assert board.winner() == "O"

def test_X_row2():
    board = TicTacToeBoard()

    board.mark("X", 4)
    board.mark("X", 5)
    board.mark("X", 6)

    assert board.winner() == "X"

def test_O_row3():
    board = TicTacToeBoard()

    board.mark("O", 7)
    board.mark("O", 8)
    board.mark("O", 9)

    assert board.winner() == "O"

def test_X_row3():
    board = TicTacToeBoard()

    board.mark("X", 7)
    board.mark("X", 8)
    board.mark("X", 9)

    assert board.winner() == "X"

def test_O_col1():
    board = TicTacToeBoard()

    board.mark("O", 1)
    board.mark("O", 4)
    board.mark("O", 7)

    assert board.winner() == "O"

def test_X_col1():
    board = TicTacToeBoard()

    board.mark("X", 1)
    board.mark("X", 4)
    board.mark("X", 7)

    assert board.winner() == "X"

def test_O_col2():
    board = TicTacToeBoard()

    board.mark("O", 2)
    board.mark("O", 5)
    board.mark("O", 8)

    assert board.winner() == "O"

def test_X_col2():
    board = TicTacToeBoard()

    board.mark("X", 2)
    board.mark("X", 5)
    board.mark("X", 8)

    assert board.winner() == "X"

def test_O_col3():
    board = TicTacToeBoard()

    board.mark("O", 3)
    board.mark("O", 6)
    board.mark("O", 9)

    assert board.winner() == "O"

def test_X_col3():
    board = TicTacToeBoard()

    board.mark("X", 3)
    board.mark("X", 6)
    board.mark("X", 9)

    assert board.winner() == "X"

def test_O_dia1():
    board = TicTacToeBoard()

    board.mark("O", 1)
    board.mark("O", 5)
    board.mark("O", 9)

    assert board.winner() == "O"

def test_X_dia1():
    board = TicTacToeBoard()

    board.mark("X", 1)
    board.mark("X", 5)
    board.mark("X", 9)

    assert board.winner() == "X"

def test_O_dia2():
    board = TicTacToeBoard()

    board.mark("O", 3)
    board.mark("O", 5)
    board.mark("O", 7)

    assert board.winner() == "O"

def test_X_dia2():
    board = TicTacToeBoard()

    board.mark("X", 3)
    board.mark("X", 5)
    board.mark("X", 7)

    assert board.winner() == "X"

