from . import Executor


class DfExecutor(Executor):
    def __init__(self):
        super().__init__()
        self._terminal = 'df'
        self.keys = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']
