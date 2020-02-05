from random import randint


class PwdGenerator:
    __abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '-', '_', '*', '^', '=', '+', '.', '?', '!']

    def __init__(self, size=0, pattern=None):
        """
        :param size: int >= 0 define the len of the password
        :param pattern: string like "$$$$-$$$$" for a password like "super-hero"

        """
        if size >= 0:
            self.size = size
        else:
            self.size = 1
        self.pwd = ""
        self.generated = False
        self.pattern = pattern

    def __str__(self):
        if self.generated:
            return self.pwd
        else:
            return "Not yet generated"

    def get_symb_list(self):
        return self.__abc

    def set_size(self, new_size):
        """
        :param new_size: int >= 0
        """
        if new_size >= 0 and self.pattern is None:
            self.size = new_size
            self.generate()

    def generate(self):
        if not self.generated:
            if self.pattern is None:
                for i in range(self.size):
                    self.pwd += self.__abc[randint(0, len(self.__abc) - 1)]
            else:
                for char in self.pattern:
                    if char == '$':
                        self.pwd += self.__abc[randint(0, len(self.__abc) - 1)]
                    else:
                        self.pwd += char
                if len(self.pwd) != self.size:
                    self.size = len(self.pwd)
            self.generated = True
        else:
            self.pwd = ""
            self.generated = False
            self.generate()

    def gen_pwd_file(self, max_len):
        """
        :param max_len: int maximum password length
        create a dictionary with all possibilities of password in a gave length or less
        """
        # TODO
        return
