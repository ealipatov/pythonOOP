from utils import Utils
import datetime


class TestService:
    def __init__(self, repo):
        self.repo = repo

    ADMIN_ACCESS = "admin_access"
    STUDENT_ACCESS = "student_access"

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
        # users_mark[login] = users_mark.get(login, []) + [(date_now, mark)]

        print(f"Правильных ответов: {right_answer}, оценка: {mark}")

    @staticmethod
    def show_menu(menu, user):
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
                    TestService.start_test(user)
                elif user_access == TestService.STUDENT_ACCESS and chosen_item == 2:
                    pass
                elif user_access == TestService.ADMIN_ACCESS and chosen_item == 1:
                    show_average_info()
                elif user_access == TestService.ADMIN_ACCESS and chosen_item == 2:
                    show_users_info()
                elif chosen_item == 10:
                    if user_access == TestService.STUDENT_ACCESS:
                        save_data()
                        print("данные сохранены")
                    print("Работы программы завершена.")
                    return
                else:
                    print("Выбран некорректный пункт меню")
            except Exception as error:
                print(error)
