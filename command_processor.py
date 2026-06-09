from lesson_parser import LessonParser


class CommandProcessor:

    def __init__(self, lessons):
        self.lessons = lessons

    def execute(self, filename):

        parser = LessonParser()

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                print("COMMAND:", line)

                if line.startswith("ADD "):

                    lesson = parser.parse(
                        line[4:]
                    )

                    self.lessons.append(
                        lesson
                    )

                    print("ADD OK")

                elif line.startswith("REM "):

                    teacher = line[4:]

                    self.lessons = [
                        lesson
                        for lesson in self.lessons
                        if lesson.teacher != teacher
                    ]

                    print("REM OK")

                elif line.startswith("SAVE "):

                    self.save(
                        line[5:]
                    )

                    print("SAVE OK")

        return self.lessons

    def save(self, filename):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            for lesson in self.lessons:

                file.write(
                    f'Lesson {lesson.date} {lesson.time} "{lesson.teacher}"\n'
                )