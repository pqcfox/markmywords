from unittest import TestCase

import markmywords

texts = [
    'This is an example sentence. So is this.',
    'Semicolons are important; they provide structure.'
    'Punctuation should be kept with individual words.',
    'In fact, all words should be split around spaces.',
    'And symbols, like $100, should be kept together.'
]

class TestMarkov(TestCase):

    def setUp(self):
        self.markovs = []
        for text in texts:
            markov = markmywords.Markov(text, 2)
            self.markovs.append(markov)

    def test_valid_chain_keys(self):
        for markov, text in zip(self.markovs, texts):
            for key in markov._chain.keys():
                for word in key:
                    assert word in key

    def test_valid_chain_values(self):
        for markov, text in zip(self.markovs, texts):
            for value in markov._chain.values():
                assert value in text 

    def test_valid_generated_words(self):
        for markov, text in zip(self.markovs, texts):
            generated_text = markov.generate(50)
            for generated_word in generated_text.split(' '):
                assert generated_word in text
