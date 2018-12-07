import unittest
from ner.neuralNetwork.recurrentNeuralNetwork import RecurrentNeuralNetwork


class TestRecurrentNeuralNetwork(unittest.TestCase):
    def setUp(self):
        self.model = RecurrentNeuralNetwork()

    def test_build_sequence(self):
        self.assertIsInstance(self.model, RecurrentNeuralNetwork)

if __name__ == '__main__':
    unittest.main()