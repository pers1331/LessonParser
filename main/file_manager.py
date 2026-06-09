import os
from lesson_parser import LessonParser


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

                if line:
                    lessons.append(
                        parser.parse(line)
                    )

        return lessons