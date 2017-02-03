from unittest import TestCase
from CODE.Functions.date_time import DateTime

DT = DateTime()


class TestDateTime(TestCase):
    def test_get_date(self):
        self.assertIsNone(DT.get_date())


    def test_get_time(self):
        self.assertIsNone(DT.get_time())


    def test_get_datetime(self):
        self.assertIsNone(DT.get_datetime())
