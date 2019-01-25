import unittest
import os

from ner.document import Vectorizer
from ner.document import Document
from ner.neuralNetwork.recurrentNeuralNetwork import RecurrentNeuralNetwork
from ner.parser import EnglishNerParser

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

file = "C:\\Users\\Adrian\\test.txt"

class TestRecurrentNeuralNetwork(unittest.TestCase):

    '''def setUp(self):
        #with open(file, "r", encoding="utf-8") as fn:
            #content = fn.read()
            #doc = Document().create_from_text(file)
            #doc = EnglishNerParser().read(content)
            word_embeddings = Vectorizer("C:\\Users\\Adrian\\glove.6B.50d.txt")
            input_shape = {
                'word': (10,10),
                'shape': (2,2)
            }
            out_shape = (2,2)
            self.model = RecurrentNeuralNetwork.build_sequence(word_embeddings.word_embedding, input_shape, out_shape)'''

    def test_build_sequence(self):
        word_embeddings = Vectorizer("C:\\Users\\Adrian\\glove.6B.50d.txt")
        input_shape = {
            'pos': (10, 10),
            'shape': (2, 2)
        }
        out_shape = 2
        self.assertIsInstance(RecurrentNeuralNetwork.build_sequence(word_embeddings.word_embedding, input_shape, out_shape),
                              RecurrentNeuralNetwork)

if __name__ == '__main__':
    unittest.main()