import argparse

from parsers import BaseParsing, RisingErrorArgparse
from executors import *


parser = RisingErrorArgparse()
group = parser.add_mutually_exclusive_group()
group.add_argument('--human', action='store_true', default=None)
group.add_argument('--inode', action='store_true', default=None)

try:
    args = parser.parse_args()
    command = create_executor(inode=args.inode)
    command.make_result()
    result = BaseParsing(command.result, command.keys)
    result.print_json()

except Exception as e:
    result = BaseParsing(None, None, error=str(e))
    result.print_json()
