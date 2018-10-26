from ner_parser.parser import Parser
from named_entites.document import Document

class EnglishNerParser(Parser):
    def read(self, content: str) -> Document:
        """Reads the content of a NER/POS data file and returns one document instance per document it finds."""
        documents = []

        # 1. Split the text in documents using string '-DOCSTART- -X- O O' and loop over it
        
        # 2. Slit lines and loop over
        # 3. Make vectors of tokens and labels (colunn 4) and at the '\n\n' make a sentence
        # 4. Create a Document object

        return documents