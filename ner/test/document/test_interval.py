import unittest
from ner.document import Interval

class TestInterval(unittest.TestCase):
    def setUp(self):
        self.Object = Interval(None, 0,10)

    def test_intersection(self):
        self.fail()
        #TODO: To be implemented

    def test_overlaps(self):
        self.fail()
        # TODO: To be implemented

    def test_shift(self):
        self.fail()
        # TODO: To be implemented

if __name__ == '__main__':
    unittest.main()