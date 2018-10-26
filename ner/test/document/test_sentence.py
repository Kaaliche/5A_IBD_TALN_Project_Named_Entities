import unittest
from ner.document import Sentence

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.object = Sentence("hello world", 0, 11)

    def test_tokens(self):
#        self.assertEqual(self.object.tokens, "hello world", "wrong text")
        # TODO: To be implemented
        NotImplementedError
if __name__ == '__main__':
    unittest.main()