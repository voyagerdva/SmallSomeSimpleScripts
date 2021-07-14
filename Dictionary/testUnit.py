import unittest
from fixtures import fixtures as fx
import dictionary as dc

class myTestQuickSort(unittest.TestCase):
    def test_partKeysEqualValues(self):
        (key, value, dicEtalon) = fx.fixtureKeysEqualValues()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

    def test_partKeysLongerValues(self):
        (key, value, dicEtalon) = fx.fixtureKeysLongerValues()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

    def test_partKeysShorterValues(self):
        (key, value, dicEtalon) = fx.fixtureKeysShorterValues()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

    def test_partKeysValuesEmpty(self):
        (key, value, dicEtalon) = fx.fixtureKeysValuesEmpty()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

    def test_partKeysEmptyOnly(self):
        (key, value, dicEtalon) = fx.fixtureKeysEmptyOnly()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

    def test_partValuesEmptyOnly(self):
        (key, value, dicEtalon) = fx.fixtureValuesEmptyOnly()
        dicResult = dc.dictionary(key, value)
        self.assertEqual(dicEtalon, dicResult)

if __name__ == '__main__':
    unittest.main()