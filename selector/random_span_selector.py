from typing import List, Tuple

from numpy.random import default_rng

from .selector import Selector
from .utils import tokenize


class RandomSpanSelector(Selector):
    """
    Randomly selects a span of words.
    """

    def __init__(self, mu: float, sigma: float) -> None:
        """
        Initializes random span selector with the given variance.
        :param mu: The mean to use when sampling proportion lengths from a
            normal distrbution.
        :param sigma: The standard deviation to use when sampling.
        """
        self.mu = mu
        self.sigma = sigma
        self.rng = default_rng()

    def __call__(self, sentence: str) -> List[Tuple[int, int]]:
        """
        Selects spans of sentences to replace.
        :param sentence: The sentence to process.
        :return: A list of non-overlapping spans to substitute.
        """
        n = len(sentence)
        length = int(self.rng.normal(self.mu, self.sigma) * n)
        if n - length <= 0:
            return []
        start = self.rng.integers(0, n - length)
        end = start + length

        tokens = tokenize(sentence)

        s_index, e_index = 0, n
        for t, (s, e) in tokens:
            if s <= start <= e:
                s_index = s
            if s <= end <= e:
                e_index = e
        return [(s_index, e_index)]
