import Script.pwd_generator as G
from random import randint as rint
import unittest


class TestPasswordGenerator(unittest.TestCase):
    def testPasswordSize(self):
        for i in range(300):
            size = rint(0, rint(20, 300))
            pwd = G.PwdGenerator(size)
            pwd.generate()
            self.assertEqual(size, pwd.size, "Fail on test: " + str(i))