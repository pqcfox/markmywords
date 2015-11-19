class Markov:
    def __init__(self, text, degree):
        self.text = text 
        self.degree = degree
        self._chain = self._make_chain(text, degree)

    @staticmethod
    def _make_chain(text, degree):
        chain = {}
        words = text.split(' ')
        for i in range(len(words) - degree):
            inputs = tuple(words[i:(i + degree)])
            output = words[i + degree]
            chain[inputs] = output
        return chain

    def generate(self, word_count):
        pass
