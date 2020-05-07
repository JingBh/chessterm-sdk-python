from math import ceil

from .http import request
from .model import Model


class Board(Model):

    def chesspos_cut(self, cut):
        """把棋子状态 (chesspos) 切割为每个元素长度为 `cut` 的列表"""

        result = []
        chunk_count = ceil(len(self.chesspos) / cut)
        for i in range(chunk_count):
            result.append(self.chesspos[i * cut:(i + 1) * cut])
        return result

    def get_data(self):
        """从服务器获取棋盘最新数据"""

        self.data = request("GET", "boards/%s" % self.id, params={
            "json": "true"
        })

        return self

    def set_data(self, data):
        """
        向服务器上传棋盘数据
        `data` 若为字符串，则表示更改后的棋子状态 (chesspos)
        """

        if type(data) == str:
            data = {
                "chesspos": data
            }

        return request("PATCH", "boards/%s" % self.id, data=data)

    @staticmethod
    def get(board_id):
        """根据 Board ID 获取棋盘信息"""

        return Board({
            "id": board_id
        }).get_data()

    @staticmethod
    def get_by_user_and_game(user_id, game_id):
        """通过 棋盘码 和 Game ID 获取棋盘信息"""

        info = request("GET", "user/getBoard", params={
            "id": user_id,
            "game": game_id
        })

        if "board" in info and info["board"]:
            return Board(info["board"])
        else:
            raise ValueError("Board not found.")
