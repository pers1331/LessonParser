import re
from models.lesson import Lesson
from utils.validator import is_valid_date, is_valid_time


class LessonParser:
    def parse(self, text):
        pattern = r'^(\w+)\s+(\d{4}\.\d{2}\.\d{2})\s+(\d{2}:\d{2})\s+"([^"]+)"$'

        match = re.match(pattern, text)

        date = match.group(2)
        time = match.group(3)

        if not is_valid_date(date):
            raise ValueError("Неверная дата")

        if not is_valid_time(time):
            raise ValueError("Неверное время")

        return Lesson(
            date,
            time,
            match.group(4)
        )