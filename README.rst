markmywords
-----------

This library is nothing more and nothing less than a simple Markov chain text generator.

>>> from markmywords import Markov
>>> with open('declaration.txt', 'r') as f:
...     text = f.read()
>>> m = Markov(text, degree=2)
>>> m.generate(max_words=13)
"petitioned for redress in the meantime exposed to all the dangers of invasion" 
