import datetime
import os
import json
import pandas as pandas
from abc import ABC, abstractmethod
from entities import Student


class StudentRepo(ABC):
    @abstractmethod
    def load_all_students(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_menu(self):
        pass

    @abstractmethod
    def show_users_info(self):
        pass


class StudentRepoXlsx(StudentRepo):
    DATA_FILE = "students_mark.xlsx"
    INIT_DATA = "initial_config.json"

    def get_config(self):
        with open(self.INIT_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def load_init_students(self, students):
        all_user = {}
        initial_users = self.get_config()["users"]

        for login, data in initial_users.items():
            if login in students:
                marks = students[login]
                student = Student(
                    name=login,
                    password=data["password"],
                    access_level=data["access_level"],
                    marks=marks
                )
            else:
                student = Student(
                    name=login,
                    password=data["password"],
                    access_level=data["access_level"]
                )
            all_user[login] = student

        return all_user

    def load_all_students(self):
        students = {}
        if os.path.exists(self.DATA_FILE):
            xlsx_data = pandas.ExcelFile(self.DATA_FILE)
            for sheet in xlsx_data.sheet_names:
                user_date = pandas.read_excel(xlsx_data, sheet)
                marks = user_date.values.tolist()
                students[sheet] = list(
                    map(lambda el: (datetime.datetime.strptime(el[0], "%Y-%m-%d %H:%M"), el[1]), marks)
                )
        return self.load_init_students(students)

    def save_data(self):
        pass

    def load_menu(self):
        return self.get_config()["menu"]

    def show_users_info(self):
        pass
