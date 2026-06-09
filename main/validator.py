import re


def is_valid_date(date):
    return bool(re.match(r"\d{4}\.\d{2}\.\d{2}", date))


def is_valid_time(time):
    return bool(re.match(r"\d{2}:\d{2}", time))