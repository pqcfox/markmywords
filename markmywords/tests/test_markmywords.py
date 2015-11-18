from unittest import TestCase

import markmywords

class TestMarkMyWords(TestCase):
    def test_markov_returns(self):
        s = markmywords.markov()
        self.assertTrue(isinstance(s, basestring))
