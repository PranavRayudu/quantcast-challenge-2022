#!/usr/bin/env python3
import os
import csv
from datetime import datetime
from argparse import ArgumentParser
from typing import TextIO, Tuple, List, Dict, Iterable

Logs = Iterable[Tuple[datetime, str]]


# https://stackoverflow.com/questions/11540854/file-as-command-line-argument-for-argparse-error-message-if-argument-is-not-va
def is_valid_file(parser: ArgumentParser, arg: str) -> TextIO:
    if not os.path.exists(arg):
        parser.error('File {} does not exist!'.format(arg))
    else:
        return open(arg, 'r')  # return an open file handle


# https://stackoverflow.com/questions/466345/converting-string-into-datetime
def is_valid_date(parser: ArgumentParser, arg: str) -> datetime:
    try:
        return datetime.strptime(arg, '%Y-%m-%d')
    except ValueError:
        parser.error('Date {} is not in yyyy-mm-dd format'.format(arg))


def parse_arguments():
    parser = ArgumentParser(description='returns the most active cookie for specified day')

    parser.add_argument("filename",
                        help="input file with cookie logs", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-d', '--date',
                        help='date in UTC format',
                        required=True,
                        type=lambda x: is_valid_date(parser, x))

    args = parser.parse_args()
    return args


# https://docs.python.org/3/library/csv.html
def process_logfile(file: TextIO) -> Logs:
    log_reader = csv.reader(file, delimiter=',')
    logs: Logs = []

    next(log_reader)
    for cookie, date in log_reader:
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            print('Invalid date format {}'.format(date))
        else:
            logs.append((date, cookie))

    return logs


def get_day_filter(date: datetime):
    return lambda log: log[0].date() == date.date()


def get_cookie_freq(logs: Logs) -> Dict[str, int]:
    cookie_freq: Dict[str, int] = {}
    for _, cookie in logs:
        cookie_freq[cookie] = cookie_freq.get(cookie, 0) + 1

    return cookie_freq


def get_most_common_cookie(cookie_freq: Dict[str, int]) -> List[str]:
    if len(cookie_freq) == 0:
        return []

    max_freq = max(cookie_freq.values())
    cookies = [cookie for cookie in cookie_freq if cookie_freq[cookie] == max_freq]
    return cookies


def main():
    args = parse_arguments()

    logs = process_logfile(args.filename)
    logs = filter(get_day_filter(args.date), logs)

    cookie_freq = get_cookie_freq(logs)
    most_freq_cookies = get_most_common_cookie(cookie_freq)

    print(*most_freq_cookies, sep=os.linesep)  # use linesep to be accurate for all OS


if __name__ == "__main__":
    main()
