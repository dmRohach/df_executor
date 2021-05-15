import json
from executors import *


class BaseParsing:
    def __init__(self, result, error=None):
        self.error = error
        self.keys = None
        self.result = result

    def __make_result(self):
        self.__values = self.result.split('\n')[1:-1]
        self.__result_dict = {key: [] for key in self.keys}
        for val in self.__values:
            val = val.split()
            for j in range(6):
                self.__result_dict[self.keys[j]].append(val[j])
        return self.__result_dict

    def print_json(self):
        if not self.error:
            final = {
                "status": "success",
                "error": self.error,
                "result": self.__make_result()
            }
        else:
            final = {
                "status": "failure",
                "error": self.error,
                "result": None
            }
        print(json.dumps(final, sort_keys=True, indent=4))

    @staticmethod
    def create_parser(executor, result):
        if isinstance(executor, HumanExecutor):
            parser = HumanParser(result)
        elif isinstance(executor, InodeExecutor):
            parser = InodeParser(result)
        else:
            parser = DfParser(result)
        return parser


from .rising_error_argparse import *
from .inode_parser import *
from .human_parser import *
from .df_parser import *