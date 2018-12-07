from typing import List
import os

from gensim.models import KeyedVectors

from ner.document import Document

from ner.data import DATA_DIR

class Vectorizer:
    """ Transform a string into a vector representation"""

    def __init__(self, word_embedding_path: str):
        """
        :param word_embedding_path: path to gensim embedding file
        """
        # TODO: Load word embeddings from file
        self.word_embedding = KeyedVectors.load_word2vec_format(word_embedding_path)

        # Create POS to index dictionary
        self.pos2index = {'PAD': 0, 'TO': 1, 'VBN': 2, "''": 3, 'WP': 4, 'UH': 5, 'VBG': 6, 'JJ': 7, 'VBZ': 8, '--': 9,
                          'VBP': 10, 'NN': 11, 'DT': 12, 'PRP': 13, ':': 14, 'WP$': 15, 'NNPS': 16, 'PRP$': 17,
                          'WDT': 18, '(': 19, ')': 20, '.': 21, ',': 22, '``': 23, '$': 24, 'RB': 25, 'RBR': 26,
                          'RBS': 27, 'VBD': 28, 'IN': 29, 'FW': 30, 'RP': 31, 'JJR': 32, 'JJS': 33, 'PDT': 34, 'MD': 35,
                          'VB': 36, 'WRB': 37, 'NNP': 38, 'EX': 39, 'NNS': 40, 'SYM': 41, 'CC': 42, 'CD': 43, 'POS': 44,
                          'LS': 45}
        # TODO: Create shape to index dictionary
        self.shape_dictionnary = {'NL': 0, 'NUMBER': 1, 'SPECIAL': 2, 'ALL-CAPS': 3, '1ST-CAP': 4, 'LOWER': 5, 'MISC': 6}
        # TODO: Create labels to index dictionary
        self.labels_dictonnary = {'O': 0,  'PER': 1, 'I-PER': 1, 'B-PER': 1, 'LOC': 2, 'I-LOC': 2, 'B-LOC': 2, 'ORG': 3,
                             'I-ORG': 3, 'B-ORG': 3,  'MISC': 4, 'I-MISC': 4, 'B-MISC': 4}

    def encode_features(self, documents: List[Document]):
        """
        Creates a feature matrix for all documents in the sample list
        :param documents: list of all samples as document objects
        :return: lists of numpy arrays for word, pos and shape features.
                 Each item in the list is a sentence, i.e. a list of indices (one per token)
        """
        # TODO:
        # Loop over documentsself.shape_dictionnary[token.pos],
        #    Loop over sentences
        #        Loop over tokens
        #           Convert features to indices
        #           Add to array
        #
        # return word, pos, shape
        shape_index, text_index,pos_index = [], [], []
        for doc in documents:
            text_local,shape_local, pos_local = [],[],[]
            for sentence in doc.sentences:
                for token in sentence.tokens:
                    if token.text.lower() in self.word_embedding.index2word:
                        text_local.append(self.word_embedding.index2word.index(token.text.lower()))
                    else:
                        text_local.append(0)
                    shape_local.append(self.shape_dictionnary[token.shape])
                    pos_local.append(self.pos2index[token.pos])
            text_index.append(text_local)
            shape_index.append(shape_local)
            pos_index.append(pos_local)
        return(text_index, pos_index, shape_index)


    def encode_annotations(self, documents: List[Document]):
        """
        Creates the Y matrix representing the annotations (or true positives) of a list of documents
        :param documents: list of documents to be converted in annotations vector
        :return: numpy array. Each item in the list is a sentence, i.e. a list of labels (one per token)
        """
        # Loop over documents
        #    Loop over sentences
        #        Loop over tokens
        #           Convert label to numerical representation
        #           Append to sentence
        # return labels
        num_label = []
        for doc in documents:
            for sentence in doc.sentences:
                for token in sentence.tokens:
                    num_label.append(self.labels_dictonnary[token.label])
                    pass