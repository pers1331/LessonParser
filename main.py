from file_manager import FileManager
from gui import LessonGUI


def main():
    lessons = FileManager.load_lessons(
        "lessons.txt"
    )

    app = LessonGUI(lessons)

    app.run()


if __name__ == "__main__":
    main()