class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.count


count = Counter()
print(count())
print(count())
print(count())