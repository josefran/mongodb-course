from pymongo import MongoClient


class Board(object):
    def __init__(self, board_name):
        self.id = 0
        self.name = board_name

    def set_id(self, board_id):
        self.id = board_id


class Boards(object):
    def __init__(self, db):
        self.db = db

    def create(self, board_name):
        board = Board(board_name)
        board_id = self.db.boards.insert_one({"name": board_name}).inserted_id
        board.set_id(board_id)
        return board
