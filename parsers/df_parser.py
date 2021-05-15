from . import BaseParsing


class DfParser(BaseParsing):
    def __init__(self, result):
        super().__init__(result)
        self.keys = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']