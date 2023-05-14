import random


class Utils:

    @staticmethod
    def input_login():
        login = input("Введите логин: ")
        return login

    @staticmethod
    def input_pass():
        password = input("Введите пароль: ")
        return password

    @staticmethod
    def check_login(students, login):
        if login.lower() in students.keys():
            return False
        else:
            print(f"Логин: {login} не найден")
            return True

    @staticmethod
    def check_password(student, password):
        if password == student.password:
            print("Доступ разрешен.")
            return False
        else:
            print("Неверный пароль")
            return True

    @staticmethod
    def user_authentication(students):
        login_incorrect = True
        pass_incorrect = True
        while login_incorrect:
            login = Utils.input_login()
            login_incorrect = Utils.check_login(students, login)
            if not login_incorrect:
                student = students[login]

        while pass_incorrect:
            password = Utils.input_pass()
            pass_incorrect = Utils.check_password(student, password)

        return student

    @staticmethod
    def generate_test():
        znak = ["+", "-", "*"][random.randint(0, 2)]
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f"{num1} {znak} {num2}"
        return question, eval(question)
