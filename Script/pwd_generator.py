from random import randint


class PwdGenerator:
    __abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, size):
        if size >= 0:
            self.size = size
        else:
            self.size = 1
        self.pwd = ""
        self.generated = False

    def __str__(self):
        if self.generated:
            return self.pwd
        else:
            return "Not yet generated"

    def set_size(self, new_size):
        if new_size > 0:
            self.size = new_size

    def generate(self):
        for i in range(self.size):
            self.pwd += self.__abc[randint(0, 61)]
        self.generated = True
