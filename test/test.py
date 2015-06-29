import unittest
from trello.boards import Boards
from pymongo import MongoClient


class TestBoard(unittest.TestCase):

    def setUp(self):
        client = MongoClient()
        self.db = client.mongodb_course

    def tearDown(self):
        self.db.mongodb_course.drop()

    def test_create_board(self):
        board_name = 'Board Fake'
        boards = Boards(self.db)
        board = boards.create(board_name)
        self.assertEqual(board.name, 'Board Fake')
        board_model = self.db.boards.find_one({"_id": board.id})
        self.assertEqual(board_model["name"], 'Board Fake')


if __name__ == '__main__':
    unittest.main()
