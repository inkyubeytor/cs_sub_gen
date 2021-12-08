from selector import Selector
from substitutor import Substitutor


class Pipeline:
    """
    End-to-end substitution pipeline.
    """
    def __init__(self,
                 selector: Selector,
                 substitutor: Substitutor) -> None:
        """
        Initialize with all pipeline components.
        :param selector: The span selection method for replacement.
        :param substitutor: The substitution method to use.
        """
        self.selector = selector
        self.substitutor = substitutor

    def __call__(self, sentence: str) -> str:
        """
        Processes a sentence through the pipeline.
        :param sentence: The sentence to process.
        :return: The substituted sentence.
        """
        spans = self.selector(sentence)
        return self.substitutor(sentence, spans)
