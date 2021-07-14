import unittest
import fixture as fx
import operate as oper

class TestFind(unittest.TestCase):

    def test_0(self):
        Sin, Sout = fx.fixture0()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_1(self):
        Sin, Sout = fx.fixture1()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_2(self):
        Sin, Sout = fx.fixture2()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_3(self):
        Sin, Sout = fx.fixture3()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_4(self):
        Sin, Sout = fx.fixture4()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_5(self):
        Sin, Sout = fx.fixture5()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_6(self):
        Sin, Sout = fx.fixture6()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_7(self):
        Sin, Sout = fx.fixture7()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_8(self):
        Sin, Sout = fx.fixture8()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_9(self):
        Sin, Sout = fx.fixture9()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_10(self):
        Sin, Sout = fx.fixture10()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_11(self):
        Sin, Sout = fx.fixture11()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_12(self):
        Sin, Sout = fx.fixture12()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_13(self):
        Sin, Sout = fx.fixture13()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_14(self):
        Sin, Sout = fx.fixture14()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_15(self):
        Sin, Sout = fx.fixture15()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_16(self):
        Sin, Sout = fx.fixture16()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_17(self):
        Sin, Sout = fx.fixture17()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_18(self):
        Sin, Sout = fx.fixture18()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_19(self):
        Sin, Sout = fx.fixture19()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_20(self):
        Sin, Sout = fx.fixture20()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

    def test_21(self):
        Sin, Sout = fx.fixture21()
        result = oper.find(Sin)
        self.assertEqual(result, Sout)

if __name__ == '__main__':
    unittest.main()