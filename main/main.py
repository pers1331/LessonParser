from lesson_parser import LessonParser


def main():
    text = 'Lesson 2025.06.10 09:30 "Иванов И.И."'

    parser = LessonParser()
    lesson = parser.parse(text)

    print(lesson)


if __name__ == "__main__":
    main()

