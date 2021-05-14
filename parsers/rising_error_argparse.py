import argparse


# removes the error output
class RisingErrorArgparse(argparse.ArgumentParser):

    def error(self, message):
        raise Exception(message)