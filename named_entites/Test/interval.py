import logging
import unittest

LOGGER = logging.getLogger(__name__)


class testInterval(unittest.TestCase):


    def setUp(self):
        NotImplementedError

    def intersection(self, other):
        NotImplementedError

    def overlaps(self, other):
        NotImplementedError

    def shift(self, int):
        NotImplementedError

if __name__ == '__main__':
    unittest.main()