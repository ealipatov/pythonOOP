class Animals:
    def __init__(self, name):
        self.name = name
        print(f"Animal_init {name}")


class Dog(Animals):
    def __init__(self, name):
        Animals.__init__(self, name)
        print(f"Dog_init {name}")


class Spiz(Dog):
    def __init__(self, name):
        Dog.__init__(self, name)
        print(f"Spiz_init {name}")


spiz = Spiz("Муся")
