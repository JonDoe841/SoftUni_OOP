class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(self.iterable) - 1
        self.index = len(self.iterable)
    def __iter__(self):
        return self

    def __next__(self):
        self.index -=1
        if self.index < 0:
            raise StopIteration
        return self.iterable[self.index]