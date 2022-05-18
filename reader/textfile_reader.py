from .reader import Reader


class TextFileReader(Reader):
    """
    Reader for text files on disk.
    """
    def __init__(self, path: str) -> None:
        """
        Initializes the text file reader.
        :param path: The file from which to read.
        """
        self.path = path
        self.file = open(path, "r", encoding="utf-8")

    def __next__(self) -> str:
        s = self.file.readline()
        if s:
            return s.strip()
        else:
            raise StopIteration
