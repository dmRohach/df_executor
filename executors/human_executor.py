from . import Executor


class HumanExecutor(Executor):
    def __init__(self):
        super().__init__()
        self._terminal = ['df', '-h']
        self.keys = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']