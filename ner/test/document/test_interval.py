import unittest
from ner.document import Interval

class TestInterval(unittest.TestCase):
    def setUp(self):
        self.Inter1 = Interval(0, 10)

    def test_intersection(self):
        inter1 = Interval(0, 5)
        inter2 = Interval(1, 6)
        inter3 = Interval(6, 7)
        inter4 = Interval(5,7)
        self.assertEqual(inter1.intersection(inter2), Interval(1, 5))
        self.assertEqual(inter2.intersection(inter1), Interval(1, 5))
        self.assertEqual(inter2.intersection(inter3), Interval(6, 6))
        self.assertEqual(inter2.intersection(inter4), Interval(5, 6))



    def test_overlaps(self):
        inter1 = Interval(0, 5)
        inter2 = Interval(1, 6)
        inter3 = Interval(6, 7)

        self.assertFalse(inter1.overlaps(inter2), "Overlaps is false")
        self.assertFalse(inter1.overlaps(inter1), "Overlaps is false")
        self.assertTrue(inter1.overlaps(inter3), "Overlaps is true")


if __name__ == '__main__':
    unittest.main()