import unittest

from lesson_parser import LessonParser


class TestLessonParser(unittest.TestCase):

    def setUp(self):
        self.parser = LessonParser()

    def test_valid_lesson(self):

        lesson = self.parser.parse(
            'Lesson 2025.06.10 09:30 "Иванов И.И."'
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

    def test_invalid_format(self):

        with self.assertRaises(ValueError):
            self.parser.parse(
                "BAD DATA"
            )

    def test_invalid_date(self):

        with self.assertRaises(ValueError):
            self.parser.parse(
                'Lesson 2025.99.99 09:30 "Иванов И.И."'
            )

    def test_invalid_time(self):

        with self.assertRaises(ValueError):
            self.parser.parse(
                'Lesson 2025.06.10 99:99 "Иванов И.И."'
            )


if __name__ == "__main__":
    unittest.main()