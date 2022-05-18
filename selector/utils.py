from typing import List, Tuple


def tokenize(sentence: str) -> List[Tuple[str, Tuple[int, int]]]:
    """
    Splits sentence into tokens by space.
    :param sentence: The sentence to split
    :return: A list of sentence tokens.
    """
    token_texts = sentence.split(" ")
    tokens = []
    curr = 0
    for t in token_texts:
        tokens.append((t, (curr, curr + len(t))))
        curr += len(t) + 1
    return tokens