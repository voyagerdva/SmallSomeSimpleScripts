import unittest
import fixture
from operate import find as fnd

class TestFind(unittest.TestCase):

    def test_0(self):
        Sin, Sout = fixture0()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_1(self):
        Sin, Sout = fx.fixture1()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_2(self):
        Sin, Sout = fx.fixture2()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_3(self):
        Sin, Sout = fx.fixture3()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_4(self):
        Sin, Sout = fx.fixture4()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_5(self):
        Sin, Sout = fx.fixture5()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_6(self):
        Sin, Sout = fx.fixture6()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_7(self):
        Sin, Sout = fx.fixture7()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_8(self):
        Sin, Sout = fx.fixture8()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_9(self):
        Sin, Sout = fx.fixture9()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_10(self):
        Sin, Sout = fx.fixture10()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_11(self):
        Sin, Sout = fx.fixture11()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_12(self):
        Sin, Sout = fx.fixture12()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_13(self):
        Sin, Sout = fx.fixture13()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_14(self):
        Sin, Sout = fx.fixture14()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_15(self):
        Sin, Sout = fx.fixture15()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

    def test_16(self):
        Sin, Sout = fx.fixture16()
        result = fnd.find(Sin)
        self.assertEqual(result, Sout)

if __name__ == '__main__':
    unittest.main()