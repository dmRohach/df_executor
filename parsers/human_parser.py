from . import BaseParsing


class HumanParser(BaseParsing):
    def __init__(self, result):
        super().__init__(result)
        self.keys = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']
