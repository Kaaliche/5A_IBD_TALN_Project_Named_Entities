from unittest import TestCase
from ner.data import DATA_DIR
from ner.parser import EnglishNerParser
import os

class TestEnglishNerParser(TestCase):

    def test_read(self):
        filename = os.path.join(DATA_DIR, 'files', 'eng.test.txt')
        documents = EnglishNerParser().read_file(filename)
        self.assertEqual(len(documents), 946)

    def test_read_two(self):
        filename_two = os.path.join(DATA_DIR, 'files', 'test.txt')
        documents = EnglishNerParser().read_file(filename_two)
        self.assertEqual(len(documents[0].sentences), 2)

        self.assertEqual(len(documents[0].sentences[0].tokens), 9)
        self.assertEqual(len(documents[0].sentences[1].tokens), 2)