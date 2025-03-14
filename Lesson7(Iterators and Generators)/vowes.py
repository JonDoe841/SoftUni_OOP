
class vowels:
    def __init__(self, text):
        self.text = text

        self.index = -1

    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        if self.text[self.index].lower() in "aeiuyo":
            return self.text[self.index]
        return self.__next__()
my_string = vowels('Abcedifuty0o')

for char in my_string:

    print(char)