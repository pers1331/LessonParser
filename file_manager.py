import os

from lesson_parser import LessonParser
from logger import Logger


class FileManager:

    @staticmethod
    def load_lessons(filename):

        parser = LessonParser()
        lessons = []

        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    lesson = parser.parse(line)
                    lessons.append(lesson)

                except ValueError as error:
                    Logger.log_error(line, error)

        return lessons