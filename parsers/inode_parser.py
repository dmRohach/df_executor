from . import BaseParsing


class InodeParser(BaseParsing):
    def __init__(self, result):
        super().__init__(result)
        self.keys = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']
