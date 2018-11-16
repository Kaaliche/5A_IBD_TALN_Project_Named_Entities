from ner.parser import Parser
from ner.document import Document, Interval


class EnglishNerParser(Parser):
    def read(self, content: str) -> Document:
        """Reads the content of a NER/POS data file and returns one document instance per document it finds."""
        documents = []

        for doc in content.split('-DOCSTART- -X- O O'):
            if doc == '':
                continue
            words, tag, sentences = [], [], []
            i = 0
            start_cursor = 0
            for line in doc.splitlines():
                if line.split():
                    words.append(line.split()[0])
                    tag.append(line.split()[3])
                    i += 1
                elif i != 0:
                    sentences.append(Interval(start_cursor, i))
                    start_cursor = i

        # 1. Split the text in documents using string '-DOCSTART- -X- O O' and loop over it
        # 2. Split lines and loop over
        # 3. Make vectors of tokens and labels (colunn 4) and at the '\n\n' make a sentence
        # 4. Create a Document object
            documents.append(Document.create_from_vectors(words, sentences, tag))

        return documents