#######################################################################
#
#   hou to find all same letters in string and delete it from string
#   - finally string without paired letters should remain
#
#######################################################################

import unittest


class TestFind(unittest.TestCase):

    def test_0(self):
        Sin, Sout = fixture0()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_1(self):
        Sin, Sout = fixture1()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_2(self):
        Sin, Sout = fixture2()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_3(self):
        Sin, Sout = fixture3()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_4(self):
        Sin, Sout = fixture4()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_5(self):
        Sin, Sout = fixture5()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_6(self):
        Sin, Sout = fixture6()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_7(self):
        Sin, Sout = fixture7()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_8(self):
        Sin, Sout = fixture8()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_9(self):
        Sin, Sout = fixture9()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_10(self):
        Sin, Sout = fixture10()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_11(self):
        Sin, Sout = fixture11()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_12(self):
        Sin, Sout = fixture12()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_13(self):
        Sin, Sout = fixture13()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_14(self):
        Sin, Sout = fixture14()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_15(self):
        Sin, Sout = fixture15()
        result = find(Sin)
        self.assertEqual(result, Sout)

    def test_16(self):
        Sin, Sout = fixture16()
        result = find(Sin)
        self.assertEqual(result, Sout)



P = ["", "q", "qw", "qq", "qqq", "qqqq", "qqw", "qqww", "qqwqqw", "qqwwee", "qqweertty", "qwe", "qwwerrtyyu", "19", "11"]

def fixture0():
    Sin = ""
    Sout = ""
    return Sin, Sout

def fixture1():
    Sin = "q"
    Sout = "q"
    return Sin, Sout

def fixture2():
    Sin = "qw"
    Sout = "qw"
    return Sin, Sout


def fixture3():
    Sin = "qq"
    Sout = ""
    return Sin, Sout


def fixture4():
    Sin = "qqq"
    Sout = "q"
    return Sin, Sout


def fixture5():
    Sin = "qqqq"
    Sout = ""
    return Sin, Sout


def fixture6():
    Sin = "qqw"
    Sout = "w"
    return Sin, Sout


def fixture7():
    Sin = "qqww"
    Sout = ""
    return Sin, Sout


def fixture8():
    Sin = "qqwqqw"
    Sout = ""
    return Sin, Sout

def fixture9():
    Sin = "qqwwee"
    Sout = ""
    return Sin, Sout

def fixture10():
    Sin = "qqweertty"
    Sout = "wry"
    return Sin, Sout

def fixture11():
    Sin = "qwe"
    Sout = "qwe"
    return Sin, Sout

def fixture12():
    Sin = "qwwerrtyyu"
    Sout = "qetu"
    return Sin, Sout

def fixture13():
    Sin = "19"
    Sout = "19"
    return Sin, Sout

def fixture14():
    Sin = ""
    Sout = ""
    return Sin, Sout

def fixture15():
    Sin = "qwewwrrertrghghvvvvv"
    Sout = "qwrtrghghv"
    return Sin, Sout

def fixture16():
    Sin = "qwqwqwqwqwqwqwq"
    Sout = "qwqwqwqwqwqwqwq"
    return Sin, Sout


def find(S):
    i = 0
    while i < len(S) - 1:
        if S[i] == S[i + 1]:
            S1 = S[:i] + S[(i + 2):]
            S = S1
            i = -1
        i += 1
    print(f"output string = '{S}'")
    return S