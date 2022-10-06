class a:
    def __init__(self) -> None:
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.n < 999:
            self.n += 1
            return self.n


b = a()
c = iter(b)
print(next(c))
