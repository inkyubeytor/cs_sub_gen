from typing import List, Tuple


class Substitutor:
    """
    Applies substitutions to spans of tokens.
    """
    def __call__(self, sentence: str, spans: List[Tuple[int, int]]) -> str:
        """
        Computes replacements for identified spans and substitutes them for the
        original tokens.
        :param sentence: The original sentence.
        :param spans: The spans to replace.
        :return: The sentence with token spans replaced.
        """
        n = len(sentence)
        endpoints = {s for s, _ in spans} | {e for _, e in spans} | {0, n}
        endpoints = sorted(endpoints)
        endpoints = [(s, e) for s, e in zip(endpoints, endpoints[1:])]
        spans = set(spans)
        new_tokens = []
        for s, e in endpoints:
            if (s, e) in spans:
                new_token = self._get_substitute(sentence[s:e])
            else:
                new_token = sentence[s:e]
            new_tokens.append(new_token)
        return self._join(new_tokens)

    def _get_substitute(self, span: str) -> str:
        """
        Returns substitute for a single span.
        :param span: The span to substitute.
        :return: The substituted string.
        """
        raise NotImplementedError

    def _join(self, tokens: List[str]) -> str:
        """
        Joins a list of tokens into a single sentence.
        :param tokens: The tokens to join.
        :return: The single string sentence.
        """
        raise NotImplementedError
