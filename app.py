from parsers import BaseParsing, RisingErrorArgparse
from executors import *


parser = RisingErrorArgparse()
group = parser.add_mutually_exclusive_group()
group.add_argument('--human', action='store_true', default=None)
group.add_argument('--inode', action='store_true', default=None)


try:
    args = parser.parse_args()
    executor = Executor.create_executor(human=args.human, inode=args.inode)
    executor.make_result()
    result = BaseParsing.create_parser(executor, executor.result)
    result.print_json()

except Exception as e:
    result = BaseParsing(None, error=str(e))
    result.print_json()
