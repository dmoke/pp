def myGen():
    yield 1
    yield 2
    yield 3


gen = myGen()

print(next(gen))
print(next(gen))
