from unittest import TestCase
from code.Functions.calculator import Math

class TestMath(TestCase):
    def test_math_add_symbol(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 2 + 6"
        self.assertTrue(Math.math(self, command))

    def test_math_add_text(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 2 plus 6"
        self.assertTrue(Math.math(self, command))

    def test_math_subtract_symbol(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 2 - 6"
        self.assertTrue(Math.math(self, command))

    def test_math_subtract_text(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 2 minus 6"
        self.assertTrue(Math.math(self, command))


    def test_math_multiply_text(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 2 times 6"
        self.assertTrue(Math.math(self, command))

    def test_math_divide_text(self):
        """tests that two numbers are added correctly with the correct command"""
        command = "calculate 6 divided by 2"
        self.assertTrue(Math.math(self, command))

        command = "calculate 6 divided by 0"
        with self.assertRaises(ZeroDivisionError):
            Math.math(self, command)

    def test_math_exceptions(self):
        command = "calculate 6 divide 2"
        with self.assertRaises(ValueError):   # command is 4 words
            Math.math(self, command)

        command = "calculate 6 wrong text 2"    # command is 5 words
        with self.assertRaises(ValueError):
            Math.math(self, command)

        command = "calculate 6 wrong wrong text 2"  # command is 6 words
        with self.assertRaises(ValueError):
            Math.math(self, command)

