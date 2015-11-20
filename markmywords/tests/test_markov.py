#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re

from markmywords import Markov

CHAIN_LENGTH = 50
DEGREE = 5

lines = [
    u'An example line can be really simple.',
    u'0r c0nt@ain symbols...',
    u'It  can    be p00rly spaaaaced.',
    u'^^^^^  ~~ 328 2nzna2 \n 3333 %% 0',
    u'❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ € ☎ ⚑ ❄ ♫ ✂'
]

markovs = [Markov(line, DEGREE) for line in lines]

def test_text_input_empty():
    with pytest.raises(ValueError):
        Markov('', DEGREE)

@pytest.mark.parametrize('markov', markovs)
def test_valid_generated_words(markov):
    words = markov.generate(CHAIN_LENGTH).split()
    check_valid_generated_words(markov, words)

@pytest.mark.parametrize('markov', markovs)
def test_valid_generated_words_with_seed(markov):
    seed = markov.text.split()[:markov.degree]
    words = markov.generate(CHAIN_LENGTH, seed=seed).split()
    check_valid_generated_words(markov, words)

def check_valid_generated_words(markov, words):
    for i in range(len(words) - markov.degree):
        chained_words = words[i:(i + markov.degree)]
        escaped_words = [re.escape(word) for word in chained_words]
        pattern = '\s+'.join(escaped_words)
        results = re.search(pattern, markov.text)
        assert results is not None

@pytest.mark.parametrize('markov', markovs)
def test_generated_words_length(markov):
    words = markov.generate(CHAIN_LENGTH).split()
    assert len(words) <= CHAIN_LENGTH

@pytest.mark.parametrize('markov', markovs)
def test_generated_words_start_with_seed(markov):
    seed = markov.text.split()[:markov.degree]
    words = markov.generate(CHAIN_LENGTH, seed=seed).split()
    assert words[:markov.degree] == seed
