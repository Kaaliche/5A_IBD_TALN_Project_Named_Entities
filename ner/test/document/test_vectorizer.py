import os
from ner.document import Vectorizer

from unittest import TestCase

from ner.data import DATA_DIR
from ner.parser import EnglishNerParser

class TestVectorizer(TestCase):


    def test_read(self):
        filename = os.path.join(DATA_DIR, 'files', 'test.txt')
        parse = EnglishNerParser().read_file(filename)
        path_embeding = os.path.join(DATA_DIR, 'files', 'glove.6B.50d.txt')

        word, pos, shape = Vectorizer(path_embeding).encode_features(parse)

        self.assertEqual(len(word), 2)

        Vectorizer(path_embeding).encode_annotations(parse)
