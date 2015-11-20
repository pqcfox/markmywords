from markmywords import Markov

CHAIN_LENGTH = 50

def test_text_input_none():
    with raises(TypeError):
        Markov(None)

def test_text_input_integer():
    with raises(TypeError):
        Markov(42)

def test_valid_generated_words(text, markov):
    words = markov.generate_text(CHAIN_LENGTH).split(' ')
    check_valid_generated_words(text, words)

def test_valid_generated_words_with_seed(text, markov):
    seed = text.split(' ')[:markov.degree]
    words = markov.generate(CHAIN_LENGTH, seed=seed).split(' ')
    check_valid_generated_words(text, words)

def check_valid_generated_words(text, words):
    for word in words:
        assert word in text
    assert len(words) == CHAIN_LENGTH 
