from .http import request
from .model import Model


class Game(Model):

    @staticmethod
    def get(game_id):
        info = request("GET", "games/%s" % game_id)
        return Game(info)
