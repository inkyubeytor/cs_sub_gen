from string import punctuation
from typing import List

from .substitutor import Substitutor


class LexiconSubstitutor(Substitutor):
    """
    Applies substitutions with dictionary switching.
    """
    def __init__(self, dict_path: str) -> None:
        """
        Initializes the substitutor by reading a dictionary from disk.
        :param dict_path: The path to the dictionary to use.
        """
        with open(dict_path, "r", encoding="utf-8") as f:
            self.lexicon = {" ".join(l): r for *l, r in
                            map(lambda s: s.split(), f.readlines())}

        self.sub = lambda x: self.lexicon.get(x.lower(), x.lower())

    def _get_substitute(self, span: str) -> str:
        """
        Returns substitute for a single span.
        :param span: The span to substitute.
        :return: The substituted string.
        """
        return " ".join(self._get_substitute_token(s) for s in span.split())

    def _get_substitute_token(self, text: str) -> str:
        """
        Returns substitute for a single token.
        :param text: The text to substitute.
        :return: The substituted text.
        """
        if len(text) == 0:
            return ""
        if not text[0] in punctuation and not text[-1] in punctuation:
            return self.sub(text)

        s = min((i for i, c in enumerate(text) if c not in punctuation),
                default=0)
        e = max((j for j, c in enumerate(text) if c not in punctuation),
                default=len(text))
        sub = self.sub(text[s:e])
        return f"{text[:s]}{sub}{text[e:]}"

    def _join(self, tokens: List[str]) -> str:
        """
        Joins a list of tokens into a single sentence.
        :param tokens: The tokens to join.
        :return: The single string sentence.
        """
        return " ".join(tokens)
