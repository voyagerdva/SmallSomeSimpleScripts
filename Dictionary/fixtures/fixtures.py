def fixtureKeysEqualValues():
    key = ['a', 'b', 'c', 'd', 'e']
    value = [1, 2, 3, 4, 5]
    dicEtalon = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    return (key, value, dicEtalon)

def fixtureKeysLongerValues():
    key = ['a', 'b', 'c', 'd', 'e']
    value = [1, 2, 3]
    dicEtalon = {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': None}
    return (key, value, dicEtalon)

def fixtureKeysShorterValues():
    key = ['a', 'b', 'c', 'd', 'e']
    value = [1, 2, 3, 4, 5, 6, 7, 8]
    dicEtalon = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    return (key, value, dicEtalon)

def fixtureKeysValuesEmpty():
    key = []
    value = []
    dicEtalon = {}
    return (key, value, dicEtalon)

def fixtureKeysEmptyOnly():
    key = []
    value = [1, 2, 3, 4, 5, 6, 7, 8]
    dicEtalon = {}
    return (key, value, dicEtalon)

def fixtureValuesEmptyOnly():
    key = ['a', 'b', 'c', 'd', 'e']
    value = []
    dicEtalon = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
    return (key, value, dicEtalon)