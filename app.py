import argparse

from parsers import BaseParsing
from executors import Executor, HumanExecutor, InodeExecutor


# removes the error output
class NewParser(argparse.ArgumentParser):

    def error(self, message):
        raise Exception(message)


parser = NewParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--human', action='store_true', default=None)
group.add_argument('--inode', action='store_true', default=None)

try:
    args = parser.parse_args()
    if args.human:
        command = HumanExecutor()
    elif args.inode:
        command = InodeExecutor()
    else:
        command = Executor()
    command.make_result()
    result = BaseParsing(command.result, command.keys)
    result.print_json()

except Exception as e:
    result = BaseParsing(None, None, error=str(e))
    result.print_json()
