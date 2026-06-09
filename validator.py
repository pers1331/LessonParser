import re

def is_valid_date(date):
    pattern = r'^\d{4}\.\d{2}\.\d{2}$'
    return bool(re.match(pattern, date))

def is_valid_time(time):
    pattern = r'^\d{2}:\d{2}$'
    return bool(re.match(pattern, time))