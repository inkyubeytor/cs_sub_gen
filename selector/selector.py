from typing import List, Tuple


class Selector:
    """
    Base class for selectors selecting spans to replace. Spans are inclusive on
    the lower end and exclusive on the upper end.
    """

    def __call__(self, sentence: str) -> List[Tuple[int, int]]:
        """
        Selects spans of sentences to replace.
        :param sentence: The sentence to process.
        :return: A list of non-overlapping spans to substitute.
        """
        raise NotImplementedError
