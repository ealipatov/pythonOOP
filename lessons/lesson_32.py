def on_table_light():
    try:
        1 / 0
        print("Настольная лампа включена")
    except Exception as error:
        print(f"Ошибка: {error}")


def on_lightning():
    print("Свет вкл")
    on_table_light()


def run():
    print("Что-то включилось")
    on_lightning()


run()


class MyException(Exception):
    pass


try:
    raise MyException("any text")
except Exception as error:
    print(f"Ошибка: {error}")
