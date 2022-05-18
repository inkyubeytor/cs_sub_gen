import time
from typing import List
from englisttohindi.englisttohindi import EngtoHindi

from .substitutor import Substitutor


class E2HSubstitutor(Substitutor):
    """
    Applies substitutions with englisttohindi (sic) translation.
    """

    def _get_substitute(self, span: str) -> str:
        """
        Returns substitute for a single span.
        :param span: The span to substitute.
        :return: The substituted string.
        """
        stripped_span = span.strip()
        if not len(stripped_span):
            return ""
        # delay so translate API does not time out
        time.sleep(1.0)
        translation = EngtoHindi(message=span.strip()).convert
        if translation:
            return translation
        else:
            print(span)
            return ""

    def _join(self, tokens: List[str]) -> str:
        """
        Joins a list of tokens into a single sentence.
        :param tokens: The tokens to join.
        :return: The single string sentence.
        """
        return " ".join(tokens)
