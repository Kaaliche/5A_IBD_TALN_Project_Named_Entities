import os
from ner.document import Vectorizer

from unittest import TestCase

from ner.data import DATA_DIR
from ner.parser import EnglishNerParser

class TestVectorizer(TestCase):


    def test_count(self):
        filename = os.path.join(DATA_DIR, 'files', 'test.txt')
        parse = EnglishNerParser().read_file(filename)
        path_embeding = os.path.join(DATA_DIR, 'files', 'glove.6B.50d.txt')
        vector = Vectorizer(path_embeding)

        word, pos, shape = vector.encode_features(parse)
        label = vector.encode_annotations(parse)

        self.assertEqual(max(len(word), len(shape), len(pos)), 2)
        self.assertEqual(len(label), 2)


    def tes_first_terme(self):
        filename = os.path.join(DATA_DIR, 'files', 'test.txt')
        parse = EnglishNerParser().read_file(filename)
        path_embeding = os.path.join(DATA_DIR, 'files', 'glove.6B.50d.txt')
        vector = Vectorizer(path_embeding)

        word, pos, shape = vector.encode_features(parse)
        label = vector.encode_annotations(parse)

        self.assertEqual(word[0][0], 644)
        self.assertEqual(pos[0][0], 38)
        self.assertEqual(shape[0][0], 3)
        self.assertEqual(label[0][0], 644)

