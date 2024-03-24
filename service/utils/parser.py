import math
from collections import Counter


def parse_text(data):
    term_frequency = Counter(data)
    inverse_frequency = {
        word: math.log(1 + 1 / (freq + 1)) for word, freq in term_frequency.items()
    }
    inverse_frequency = dict(
        sorted(inverse_frequency.items(), key=lambda x: x[1], reverse=True)
    )
    frequency = {word:(term_frequency[word], ifr) for word, ifr in inverse_frequency.items()}
    return frequency
