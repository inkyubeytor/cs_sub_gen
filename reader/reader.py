class Reader:
    """
    Base class for reading data into pipeline.
    """

    def __iter__(self):
        """
        Allows direct iteration.
        :return: The reader itself, treated as an iterator.
        """
        return self

    def __next__(self) -> str:
        """
        Yields the next read string.
        :return: A sentence string.
        """
        raise NotImplementedError
