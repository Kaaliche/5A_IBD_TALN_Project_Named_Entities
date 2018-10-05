from document.interval import Interval


class Sentence(Interval):
    """ Interval corresponding to a Sentence"""

    def __init__(self, document, start: int, end: int):
        Interval.__init__(self, start, end)
        self._doc = document

    def __repr__(self):
        return 'Sentence({}, {})'.format(self.start, self.end)

    @property
    def tokens(self):
        """Returns the list of tokens contained in a sentence"""
        return [token for token in self._doc.tokens if self.overlaps(token)]


        #for token in self._doc.tokens:
        #   if Interval.overlaps(self, token):
        #       sent_token.append(token)
        #return sent_token
        # TODO: To be implemented (tip: use Interval.overlap)
