import subprocess


class Executor:
    def __init__(self):
        self.__terminal = 'df'
        self.keys = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']
        self.error = None
        self.result = None

    @classmethod
    def create_executor(cls, human=None, inode=None):
        if human:
            executor = HumanExecutor()
        elif inode:
            executor = InodeExecutor()
        else:
            executor = cls()
        return executor

    def make_result(self):
        _command = subprocess.Popen(self.__terminal, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        self.result, self.error = [item.decode("utf-8") for item in _command]


from .human_executor import *
from .inode_executor import *

