import math
import string
from collections import Counter


def parse_file(data: str) -> list[str]:
    data = data.strip().split()
    data = (
        "".join(char for char in word if char not in string.punctuation)
        for word in data
    )
    data = (word.lower() for word in data if len(word) > 3 and not word.isdigit())
    return list(data)


def get_ft_idf(data: list[str]):
    total_length = len(data)
    counter = Counter(data)

    ft_idf = {
        word: (round(count / total_length, 5), round(math.log(1 / 1), 2))
        for word, count in counter.most_common(50)
    }

    return ft_idf
