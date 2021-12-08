from typing import List, Tuple
from random import random

from .selector import Selector
from .utils import tokenize


class RandomSelector(Selector):
    """
    Randomly selects individual words.
    """
    def __init__(self, p: float) -> None:
        """
        Initializes random selector with probability.
        :param p: The probability a given word is swapped.
        """
        self.p = p

    def __call__(self, sentence: str) -> List[Tuple[int, int]]:
        """
        Selects spans of sentences to replace.
        :param sentence: The sentence to process.
        :return: A list of non-overlapping spans to substitute.
        """
        tokens = tokenize(sentence)
        return [bounds
                for _, bounds in tokens
                if random() <= self.p]
