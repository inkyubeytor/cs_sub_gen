from typing import List


class Tokenizer:
    """
    Base class for tokenizing sentences.
    """
    def __call__(self, sentence: str) -> List[str]:
        """
        Tokenize a sentence into a list of strings.
        :param sentence: The sentence to tokenize.
        :return: A list of string tokens in order.
        """
        raise NotImplementedError
