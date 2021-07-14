import unittest

from fixtures import fixtures as fx
import fibonacсi as fb


class myTestQuickSort(unittest.TestCase):

    def test_0Term(self):
        (maxNumber, fibo, sumEven) = fx.fixture0Term()
        (fiboResult, sumEvenResult) = fb.fibonacci(maxNumber)
        self.assertEqual(fibo, fiboResult)
        self.assertEqual(sumEven, sumEvenResult)

    def test_1Terms(self):
        (maxNumber, fibo, sumEven) = fx.fixture1Term()
        (fiboResult, sumEvenResult) = fb.fibonacci(maxNumber)
        self.assertEqual(fibo, fiboResult)
        self.assertEqual(sumEven, sumEvenResult)

    def test_2Term(self):
        (maxNumber, fibo, sumEven) = fx.fixture2Term()
        (fiboResult, sumEvenResult) = fb.fibonacci(maxNumber)
        self.assertEqual(fibo, fiboResult)
        self.assertEqual(sumEven, sumEvenResult)

    def test_3Term(self):
        (maxNumber, fibo, sumEven) = fx.fixture3Term()
        (fiboResult, sumEvenResult) = fb.fibonacci(maxNumber)
        self.assertEqual(fibo, fiboResult)
        self.assertEqual(sumEven, sumEvenResult)

    def test_20Terms(self):
        (maxNumber, fibo, sumEven) = fx.fixture20Terms()
        (fiboResult, sumEvenResult) = fb.fibonacci(maxNumber)
        self.assertEqual(fibo, fiboResult)
        self.assertEqual(sumEven, sumEvenResult)

if __name__ == '__main__':
    unittest.main()
