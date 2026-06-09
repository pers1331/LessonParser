import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog

from lesson import Lesson
from command_processor import CommandProcessor


class LessonGUI:

    def __init__(self, lessons):
        self.lessons = lessons

        self.root = tk.Tk()
        self.root.title("Учебные занятия")
        self.root.geometry("700x400")

        self.tree = ttk.Treeview(
            self.root,
            columns=("date", "time", "teacher"),
            show="headings"
        )

        self.tree.heading("date", text="Дата")
        self.tree.heading("time", text="Время")
        self.tree.heading("teacher", text="Преподаватель")

        self.tree.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        add_button = tk.Button(
            button_frame,
            text="Добавить",
            command=self.add_lesson
        )

        delete_button = tk.Button(
            button_frame,
            text="Удалить",
            command=self.delete_lesson
        )

        command_button = tk.Button(
            button_frame,
            text="Команды",
            command=self.execute_commands
        )

        add_button.pack(side=tk.LEFT, padx=10, pady=10)
        delete_button.pack(side=tk.LEFT, padx=10, pady=10)
        command_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.refresh_table()

    def refresh_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for lesson in self.lessons:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    lesson.date,
                    lesson.time,
                    lesson.teacher
                )
            )

    def add_lesson(self):

        date = simpledialog.askstring(
            "Добавление",
            "Введите дату:"
        )

        time = simpledialog.askstring(
            "Добавление",
            "Введите время:"
        )

        teacher = simpledialog.askstring(
            "Добавление",
            "Введите преподавателя:"
        )

        if date and time and teacher:

            self.lessons.append(
                Lesson(
                    date,
                    time,
                    teacher
                )
            )

            self.refresh_table()

    def delete_lesson(self):

        selected = self.tree.selection()

        if selected:

            index = self.tree.index(
                selected[0]
            )

            del self.lessons[index]

            self.refresh_table()

    def execute_commands(self):

        filename = filedialog.askopenfilename(
            title="Выберите файл команд"
        )

        if not filename:
            return

        processor = CommandProcessor(
            self.lessons
        )

        self.lessons = processor.execute(
            filename
        )

        self.refresh_table()

    def run(self):
        self.root.mainloop()