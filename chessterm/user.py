from .http import request
from .model import Model
from .game import Game
from .board import Board


class User(Model):

    def get_board(self, game):
        """根据 Game ID 获取此用户对应的棋盘信息"""

        if type(game) == Game:
            game = game.id

        return Board.get_by_user_and_game(self.id, game)

    @staticmethod
    def get(user_id):
        """根据棋盘码获取用户信息"""

        info = request("GET", "user/getBoard", params={
            "id": user_id,
            "game": 1000
        })

        if "user" in info and info["user"]:
            return User(info["user"])
        else:
            raise ValueError("User not found.")
