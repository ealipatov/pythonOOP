from utils import Utils
import datetime


class TestService:
    def __init__(self, repo):
        self.repo = repo

    ADMIN_ACCESS = "ADMIN_ACCESS"
    STUDENT_ACCESS = "STUDENT_ACCESS"

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
        student.marks.append(datetime.datetime.now(), mark)
        # student.marks.append(mark)

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
            print(f"{counter}. {login}: {sum(int_marks) / len(int_marks) if len(int_marks) !=0 else 'Нет оценок'}")
            counter += 1
            for mark in data.marks:
                marks_sum += mark[1]
                marks_count += 1
        print("=" * 80)
        print(f"Средний бал по всем пользователям: {round(marks_sum / marks_count, 2)}")
        print("=" * 80)

    @staticmethod
    def show_users_info(students):
        user_name = input("Введите имя ученика: ").lower()
        if user_name in students.keys():
            marks = students[user_name]
            for mark in marks:
                print(f"Отметка: {mark[1]} получена -> {mark[0]}")
        else:
            print(f"Пользователя с именем {user_name} нет в списке")

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
                chosen_item = int(input("Выберете пункт меню: "))
                if user_access == TestService.STUDENT_ACCESS and chosen_item == 1:
                    self.start_test(user)
                elif user_access == TestService.STUDENT_ACCESS and chosen_item == 2:
                    pass
                elif user_access == TestService.ADMIN_ACCESS and chosen_item == 1:
                    self.show_average_info(students)
                elif user_access == TestService.ADMIN_ACCESS and chosen_item == 2:
                    self.show_users_info(students)
                elif chosen_item == 10:
                    if user_access == TestService.STUDENT_ACCESS:
                        self.repo.save_data(students)
                        print("данные сохранены")
                    print("Работы программы завершена.")
                    return
                else:
                    print("Выбран некорректный пункт меню")
            except Exception as error:
                print(error)
