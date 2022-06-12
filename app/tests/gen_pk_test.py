import unittest
from app.utils import generateID
from unittest import TestCase


class GenPkTest(TestCase):
    def test_func(self):
        self.asserEqual(type(generateID()), str)
        
if __name__ == '__main__':
    unittest.main()
