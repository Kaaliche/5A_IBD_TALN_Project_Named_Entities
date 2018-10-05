from unittest import TestCase
from named_entites.Document import Token

class TestToken(TestCase):
    def setUp(self):
        self.Object = Token(None, 0, 10, "pos", shape="shape", text="text")
    def test_text(self):
        self.fail()

    def test_pos(self):
        self.fail()

    def test_shape(self):
        self.fail()
