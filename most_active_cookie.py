#!/usr/bin/env python
from typing import TextIO
from argparse import ArgumentParser
import os


# https://stackoverflow.com/questions/11540854/file-as-command-line-argument-for-argparse-error-message-if-argument-is-not-va
def is_valid_file(parser: ArgumentParser, arg: str) -> TextIO:
    if not os.path.exists(arg):
        parser.error('File {} does not exist!'.format(arg))
    else:
        return open(arg, 'r')  # return an open file handle


def parse_arguments():
    parser = ArgumentParser(description='returns the most active cookie for specified day')

    parser.add_argument("filename",
                        help="input file with cookie logs", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-d', '--date', required=True, help='date in UTC format')

    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    print(args.date)
    with args.filename as file:
        for line in file:
            print(line)
    # print(args.file, args.date)


if __name__ == "__main__":
    main()
