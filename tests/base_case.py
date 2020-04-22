import unittest
from app import app
from models import db


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self) -> None:
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
