from typing import List

from .tokenizer import Tokenizer


class SplitTokenizer(Tokenizer):
    """
    A naive tokenizer using str.split().
    """
    def __call__(self, sentence: str) -> List[str]:
        return sentence.split()
