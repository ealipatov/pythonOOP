class Dog:
    def __new__(cls, *args, **kwargs):
        print(f"__new__, {cls}")
        return super().__new__(cls)

    def __init__(self):
        print(f"__init__, {self}")


dog1 = Dog()
print(dog1)


class DB:

    db_connect = None

    def __new__(cls, *args, **kwargs):
        if DB.db_connect is None:
            DB.db_connect = super().__new__(cls)
        return DB.db_connect

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f"{self.login} | {self.password} | {id(self)}"

    def safe_data(self):
        print("Save")

    def delete_date(self):
        print("Delete")


db = DB("log1", "pass1")
db2 = DB("log2", "pass2")
print(db, db2)