from random import randrange

def ranGen(size):
    res = [randrange(1, size) for i in range (size)]
    return res
