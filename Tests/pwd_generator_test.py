import Script.pwd_generator as gen
from random import randint as r_int
import unittest


class TestPasswordGenerator(unittest.TestCase):
    def testPasswordSize(self):
        for i in range(300):
            size = r_int(0, r_int(20, 300))
            pwd = gen.PwdGenerator(size)
            pwd.generate()
            self.assertEqual(size, pwd.size, "Fail on test: " + str(i))

    def testPasswordPattern(self):
        char_list = ['.', '-', '_', '?', '!', '$']
        for i in range(300):
            pattern = ""
            for j in range(r_int(0, 20)):
                pattern += char_list[r_int(0, len(char_list) - 1)]
            pwd = gen.PwdGenerator(0, pattern)
            pwd.generate()
            for k in range(len(pattern)):
                if pattern[k] != '$':
                    self.assertEqual(pattern[k], pwd.pwd[k])
