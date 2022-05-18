from typing import List

from .substitutor import Substitutor


class LexiconSubstitutor(Substitutor):
    """
    Applies substitutions with mosesdecoder translation.
    """
    def __init__(self) -> None:
        """
        Initializes the substitutor by starting a mosesdecoder server.
        """
        pass

    def _get_substitute(self, span: str) -> str:
        """
        Returns substitute for a single span.
        :param span: The span to substitute.
        :return: The substituted string.
        """
        pass

    def _join(self, tokens: List[str]) -> str:
        """
        Joins a list of tokens into a single sentence.
        :param tokens: The tokens to join.
        :return: The single string sentence.
        """
        return " ".join(tokens)
