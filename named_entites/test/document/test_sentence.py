from unittest import TestCase
from named_entites.document import Sentence

class TestSentence(TestCase):
    def setUp(self):
        self.Object = Sentence(None, 0, 10)

    def test_tokens(self):
        self.fail()
