class Lesson:
    def __init__(self, date, time, teacher):
        self.date = date
        self.time = time
        self.teacher = teacher

    def __str__(self):
        return (
            f"Дата: {self.date}\n"
            f"Время: {self.time}\n"
            f"Преподаватель: {self.teacher}"
        )