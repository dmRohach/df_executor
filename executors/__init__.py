import subprocess


def create_executor(human=None, inode=None):
    if human:
        command = HumanExecutor()
    elif inode:
        command = InodeExecutor()
    else:
        command = Executor()
    return command


class Executor:
    def __init__(self):
        self._terminal = 'df'
        self.keys = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']
        self.error = None
        self.result = None

    def make_result(self):
        _command = subprocess.Popen(self._terminal, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        self.result, self.error = [item.decode("utf-8") for item in _command]


from .human_executor import *
from .inode_executor import *

