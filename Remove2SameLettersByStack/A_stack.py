""" STACK! How it works: 

>>> push(1)
>>> push(2)
>>> push(3)
>>> size()
3
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> check()
1
>>> check()
1
>>> check()
1
>>> size()
1
>>> is_empty()
False
>>> push(1)
>>> size()
2
>>> clear()
>>> is_empty()
True

"""
_stack = []

def push(x):
    x = _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

def size():
    return len(_stack)

def check():
    x = _stack.pop()
    _stack.append(x)
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)