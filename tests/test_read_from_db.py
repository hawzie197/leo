from unittest import TestCase
from db import Database

class TestRead_from_db(TestCase):
    def test_read_from_db(self):
        command = "what is your name"
        self.assertTrue(Database.read_from_db(command))

    def test_db_exception(self):
        command = "this is an invalid keyword"
        with self.assertRaises(ValueError):
            Database.read_from_db(command)


