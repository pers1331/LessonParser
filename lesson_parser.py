import re

from lesson import Lesson
from validator import is_valid_date, is_valid_time


class LessonParser:

    def parse(self, text):

        pattern = (
            r'^(\w+)\s+'
            r'(\d{4}\.\d{2}\.\d{2})\s+'
            r'(\d{2}:\d{2})\s+'
            r'"([^"]+)"$'
        )

        match = re.match(pattern, text)

        if match is None:
            raise ValueError(
                "Неверный формат строки"
            )

        date = match.group(2)
        time = match.group(3)
        teacher = match.group(4)

        if not is_valid_date(date):
            raise ValueError(
                "Неверная дата"
            )

        if not is_valid_time(time):
            raise ValueError(
                "Неверное время"
            )

        return Lesson(
            date,
            time,
            teacher
        )