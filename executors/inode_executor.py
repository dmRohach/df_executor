from . import Executor


class InodeExecutor(Executor):
    def __init__(self):
        super().__init__()
        self.__terminal = ['df', '-i']
        self.keys = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']
