#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from collections import defaultdict, Counter


class Markov:

    def __init__(self, text, degree):
        if text.strip() == '':
            raise ValueError('Input text cannot be empty string')
        self.text = text 
        self.degree = degree
        self._chain = self._make_chain(text, degree)

    @staticmethod
    def _make_chain(text, degree):
        chain = defaultdict(Counter) 
        words = text.split()
        for i in range(len(words) - degree):
            inputs = tuple(words[i:(i + degree)])
            output = words[i + degree]
            chain[inputs][output] += 1
        return chain

    def generate(self, max_words, seed=None):
        keys = self._chain.keys()
        if len(keys) == 0:
            return self.text
        words = list(random.choice(keys)) if seed is None else seed[:]
        while len(words) < max_words:
            last_words = tuple(words[-self.degree:])
            possible_words = self._chain[last_words]
            try:
                new_word = random.choice(list(possible_words))
            except IndexError as ie:
                break
            words.append(new_word)
        return ' '.join(words)
