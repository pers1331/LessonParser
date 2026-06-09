import unittest

from lesson import Lesson


class TestLesson(unittest.TestCase):

    def test_create_lesson(self):

        lesson = Lesson(
            "2025.06.10",
            "09:30",
            "Иванов И.И."
        )

        self.assertEqual(
            lesson.date,
            "2025.06.10"
        )

        self.assertEqual(
            lesson.time,
            "09:30"
        )

        self.assertEqual(
            lesson.teacher,
            "Иванов И.И."
        )


if __name__ == "__main__":
    unittest.main()