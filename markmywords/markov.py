import random

from collections import defaultdict, Counter


class MarkovKeyError(Exception):
    pass


class Markov:

    def __init__(self, text, degree):
        self.text = text 
        self.degree = degree
        self._chain = self._make_chain(text, degree)

    @staticmethod
    def _make_chain(text, degree):
        chain = defaultdict(Counter) 
        words = text.split(' ')
        for i in range(len(words) - degree):
            inputs = tuple(words[i:(i + degree)])
            output = words[i + degree]
            chain[inputs][output] += 1
        return chain

    def generate(self, word_count, seed=None):
        if seed is None:
            keys = self._chain.keys()
            words = list(random.choice(keys))
        else:
            words = seed[:]
        while len(words) < word_count:
            last_words = tuple(words[-self.degree:])
            possible_words = self._chain[last_words]
            try:
                new_word = random.choice(list(possible_words))
            except IndexError as ie:
                error_format = "No word following {} in chain"
                raise MarkovKeyError(error_format.format(last_words))
            words.append(new_word)
        return ' '.join(words)
