import unittest
from random import choices
from time import time

import chessterm

GAME_ID = 1002  # I'm using 捉鳖, because it has a small board.
USER_ID = 1017010201  # This user is for testing, do not use it directly.
USER_NAME = "chessterm-sdk-python-test"
BOARD_ID = str(GAME_ID) + str(USER_ID)


def generate_chesspos(length: int):
    return "".join(choices(["0", "z", "Z"], k=length))


def test_board(self, board):
    self.assertIsInstance(board, chessterm.Board)
    self.assertIsInstance(board.get_data(), chessterm.Board)

    self.assertEqual(str(board.id), BOARD_ID)

    new_chesspos = generate_chesspos(5 * 5)
    board.set_data(new_chesspos)
    board.get_data()
    self.assertEqual(board.chesspos, new_chesspos)

    new_chesspos = generate_chesspos(5 * 5)
    new_clock = str(round(time()))
    board.set_data({
        "chesspos": new_chesspos,
        "clock": new_clock
    })
    board.get_data()
    self.assertEqual(board.chesspos, new_chesspos)
    self.assertEqual(board.clock, new_clock)

    cut = board.chesspos_cut(5)
    for i in range(5):
        with self.subTest(i=i):
            self.assertRegex(cut[i], r'[0zZ]{5}')


class TestUser(unittest.TestCase):

    def test_get_user(self):
        user = chessterm.User.get(USER_ID)

        self.assertIsInstance(user, chessterm.User)

        self.assertEqual(user.id, USER_ID)
        self.assertEqual(user.name, USER_NAME)

    def test_get_board(self):
        board = chessterm.Board.get(BOARD_ID)

        test_board(self, board)

    def test_get_board_by_user(self):
        user = chessterm.User.get(USER_ID)
        board = user.get_board(GAME_ID)

        test_board(self, board)

    def test_get_board_by_user_and_game(self):
        board = chessterm.Board.get_by_user_and_game(USER_ID, GAME_ID)

        test_board(self, board)

    def test_get_game(self):
        game = chessterm.Game.get(GAME_ID)

        self.assertIsInstance(game, chessterm.Game)

        self.assertEqual(game.id, GAME_ID)
        self.assertEqual(game.row, 5)
        self.assertEqual(game.column, 5)


if __name__ == '__main__':
    unittest.main()
