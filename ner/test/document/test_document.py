from unittest import TestCase
from ner.document import Document


class TestDocument(TestCase):
    def test_create_from_text(self):
        text = "This one sentence. This is an other sentence"
        doc = Document.create_from_text(text)
        self.assertEqual(len(doc.tokens), 9)
        self.assertEqual(len(doc.sentences), 2)
        self.assertEqual(doc.tokens[0].text, "This")
        self.assertEqual(doc.tokens[-1].text, "sentence")
