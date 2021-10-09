#!/usr/bin/env python3
import os
from datetime import datetime, timezone
from argparse import ArgumentParser
from typing import TextIO, Tuple, List, Dict

Logs = List[Tuple[datetime, str]]


def is_valid_file(parser: ArgumentParser, arg: str) -> TextIO:
    """
    Opens a file if it exists or else errors out
    :param parser: The CLI argument parser
    :param arg: The path to the log file
    :return: Opens and returns the log file object pointed to by `arg`
    """
    if os.path.exists(arg):
        return open(arg, 'r')
    else:
        parser.error('File {} does not exist!'.format(arg))


def is_valid_date(parser: ArgumentParser, arg: str) -> datetime:
    """
    Converts YYY-MM-DD format to `datetime`. Produces error on bad format
    :param parser: the CLI argument parser
    :param arg: the date string
    :return: datetime object ver
    """
    try:
        return datetime.strptime(arg, '%Y-%m-%d')
    except ValueError:
        parser.error('Date {} is not in yyyy-mm-dd format'.format(arg))


def parse_arguments():
    """
    Parses arguments for Most Active Cookie problem. Example: `most_active_cookie_log.csv -d 2018-12-09`
    """
    parser = ArgumentParser(description='returns the most active cookie for specified day')

    parser.add_argument('filename',
                        help='input file with cookie logs', metavar='FILE',
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-d', '--date',
                        help='date in UTC format',
                        required=True,
                        type=lambda x: is_valid_date(parser, x))

    args = parser.parse_args()
    return args


def process_logfile(log_file: TextIO) -> Logs:
    """
    Converts file into a list of logs
    :param log_file: file object formatted as a csv file
    :return: List of logs with each entry formatted as a tuple with timestamp and cookie string
    """
    logs: Logs = []

    next(log_file)
    for line_num, line in enumerate(log_file):
        cookie, date = line.strip().split(',')
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            print('Invalid date format {} on line {}'.format(date, line_num + 1))
        else:
            logs.append((date, cookie))
    log_file.close()
    return logs


def get_day_filter(date: datetime):
    """
    Returns function that returns true if parameter is same day as `date`
    :param date: datetime object
    :return: lambda function
    """
    return lambda log: log[0].astimezone(timezone.utc).date() == date.astimezone(timezone.utc).date()


def get_cookie_freq(logs: Logs) -> Dict[str, int]:
    """
    Given list of logs, returns a dictionary of cookies - count pairs
    :param logs: list of logs that consist of a cookie and its timestamp
    :return: cookie frequency dictionary
    """
    cookie_freq: Dict[str, int] = {}
    for _, cookie in logs:
        cookie_freq[cookie] = cookie_freq.get(cookie, 0) + 1

    return cookie_freq


def get_most_common_cookie(cookie_freq: Dict[str, int]) -> List[str]:
    """
    Returns a list of the highest frequency cookies
    :param cookie_freq: dictionary of cookie-count pairs
    :return: list of most occurring cookies
    """
    if len(cookie_freq) == 0:
        return []

    max_freq = max(cookie_freq.values())
    cookies = [cookie for cookie in cookie_freq if cookie_freq[cookie] == max_freq]
    return cookies


def main():
    args = parse_arguments()

    logs = process_logfile(args.filename)
    logs = list(filter(get_day_filter(args.date), logs))

    cookie_freq = get_cookie_freq(logs)
    most_freq_cookies = get_most_common_cookie(cookie_freq)
    print(*most_freq_cookies, sep=os.linesep)  # use linesep to be accurate for all OS


if __name__ == "__main__":
    main()
