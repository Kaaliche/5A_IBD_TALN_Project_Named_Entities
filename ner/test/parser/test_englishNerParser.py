from unittest import TestCase
from ner.data import DATA_DIR
from ner.parser import EnglishNerParser
import os

class TestEnglishNerParser(TestCase):

    def test_read(self):
        filename = os.path.join(DATA_DIR, 'files', 'eng.test.txt')
        documents = EnglishNerParser().read_file(filename)
        self.assertEqual(len(documents), 946)

