def on_table_light():
    1 / 0
    print("Настольная лампа включена")


def on_lightning():
    print("Свет вкл")
    on_table_light()


def run():
    print("Что-то включилось")
    on_lightning()


run()