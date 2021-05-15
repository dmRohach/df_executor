import subprocess


class Executor:
    def __init__(self):
        self._terminal = None
        self.keys = None
        self.error = None
        self.result = None

    @staticmethod
    def create_executor(human=None, inode=None):
        if human:
            executor = HumanExecutor()
        elif inode:
            executor = InodeExecutor()
        else:
            executor = DfExecutor()
        return executor

    def make_result(self):
        _command = subprocess.Popen(self._terminal, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        self.result, self.error = [item.decode("utf-8") for item in _command]


from .human_executor import *
from .inode_executor import *
from .df_executor import *

