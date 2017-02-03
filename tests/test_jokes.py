from unittest import TestCase
from CODE.Functions.joke_page import Jokes


class TestJokes(TestCase):
    def test_tell_joke(self):
        self.assertTrue(Jokes.tell_joke())


