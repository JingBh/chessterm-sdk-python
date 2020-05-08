# chessterm-sdk-python

ChessTerm SDK for Python

![Workflow Status](https://img.shields.io/github/workflow/status/JingBh/chessterm-sdk-python/Test%20and%20Build%20the%20Package)
![Version](https://img.shields.io/pypi/v/chessterm-sdk?label=version)
![Downloads](https://img.shields.io/pypi/dm/chessterm-sdk)
![Python Version](https://img.shields.io/badge/python-%E2%89%A53.4-green)
![License](https://img.shields.io/github/license/JingBh/chessterm-sdk-python)

## How to Install
```bash
pip install chessterm-sdk
```

## How to Use

There are three classes, `User`, `Game` and `Board`.

In the following examples, `user_id` is your **棋盘码**.

```python
# Import the package first
import chessterm

# ------------------------------------

# 1. Get user info.
user = chessterm.User.get(user_id)

print(user.id)  # The value of user_id
print(user.name)  # Your username

# ------------------------------------

# 2. Get game info.

game = chessterm.Game.get(1000)

print(game.title)  # Title of the game
print(game.description)  # Description of the game
print(game.row, game.column)  # Size of the board

# ------------------------------------

# 3. Get board info.

# 3.1. Get board from the user object.
board = user.get_board(1000)  # 1000 is the Game ID

# 3.2. Get board by both User ID and Game ID
board = chessterm.Board.get_by_user_and_game(user_id, 1000)  # 1000 is the Game ID

# 3.3. Get board by Board ID
board = chessterm.Board.get(board_id)

print(board.id)  # Board ID, which is useful when calling the API directly
print(board.chesspos)  # For example: 000000ZZZ0000000zzz00000

board.set_data("000000Z0Z00Z0z00z0z00000")  # Update the board

board.get_data()  # Download the latest data from the server
```

## About
See [this repository](https://github.com/JingBh/flamechess) for more information.
