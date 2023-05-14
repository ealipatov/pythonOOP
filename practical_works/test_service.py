from utils import Utils
import datetime


class TestService:
    def __init__(self, repo):
        self.repo = repo

    ADMIN_ACCESS = "ADMIN_ACCESS"
    STUDENT_ACCESS = "STUDENT_ACCESS"
    PROGRAM_STATUS = "STOP"

    @staticmethod
    def start_test(student):
        right_answer = 0
        for i in range(1, 6):
            question, answer = Utils.generate_test()
            try:
                user_answer = int(input(f"Реши пример: {question} = "))
                if user_answer == answer:
                    right_answer += 1
                    print("Правильный ответ")
                else:
                    print(f"Ошибка. Правильный ответ: {answer}")
            except Exception as error:
                print(error)
                print(" Ошибка. Введенный ответ не целое число")
        mark = right_answer * 2
        student.marks.append((datetime.datetime.now(), mark))

        print(f"Правильных ответов: {right_answer}, оценка: {mark}")

    @staticmethod
    def show_average_info(students):
        counter = 1
        marks_sum = 0
        marks_count = 0
        print("\nСредний бал по пользователям: ")
        print("=" * 80)
        for login, data in students.items():
            int_marks = list(map(lambda el: el[1], data.marks))
            print(f"{counter}. {login}: {sum(int_marks) / len(int_marks) if len(int_marks) != 0 else 'Нет оценок'}")
            counter += 1
            for mark in data.marks:
                marks_sum += mark[1]
                marks_count += 1
        print("=" * 80)
        print(f"Средний бал по всем пользователям: {round(marks_sum / marks_count, 2)}")
        print(f"Общее количество оценок по пользователям: {marks_count}")
        print("=" * 80)

    @staticmethod
    def show_users_info(students, student_name="NoName"):
        if student_name == "NoName":
            user_name = input("Введите имя ученика: ").lower()
        else:
            user_name = student_name

        if user_name in students.keys():
            marks = students[user_name].marks
            count = 1
            print(f"\nОценки ученика: {user_name}")
            for mark in marks:
                print(f"{count}. Отметка: {mark[1]} получена -> {mark[0]}")
                count += 1
            print(f"Всего оценок: {count - 1}")
        else:
            print(f"Пользователя с именем {user_name} нет в списке")

    def student_menu(self, user, students):
        chosen_item = int(input("Выберете пункт меню: "))
        if chosen_item == 1:
            self.start_test(user)
        elif chosen_item == 2:
            self.show_users_info(students, user.name)
        elif chosen_item == 10:
            self.repo.save_data(students)
            print("данные сохранены")
            print("Работы программы завершена.")
            return self.PROGRAM_STATUS
        else:
            print("Выбран некорректный пункт меню")

    def admin_menu(self, students):
        chosen_item = int(input("Выберете пункт меню: "))

        if chosen_item == 1:
            self.show_average_info(students)
        elif chosen_item == 2:
            self.show_users_info(students)
        elif chosen_item == 10:
            print("Работы программы завершена.")
            return self.PROGRAM_STATUS
        else:
            print("Выбран некорректный пункт меню")

    def show_menu(self, students, menu, user):
        while True:
            user_access = user.access_level
            current_menu = menu[user.access_level]

            print(f"\nМеню пользователя: ")
            print("=" * 80)
            for item in current_menu:
                print(f"{item}", current_menu[item])
            print("=" * 80)

            try:
                if user_access == self.STUDENT_ACCESS:
                    status = self.student_menu(user, students)
                elif user_access == self.ADMIN_ACCESS:
                    status = self.admin_menu(students)
                else:
                    status = self.PROGRAM_STATUS

                if status == self.PROGRAM_STATUS:
                    return

            except Exception as error:
                print(error)
