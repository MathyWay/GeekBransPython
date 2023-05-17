def add(a : int):
    return(a + a)


def math(op, x, y):
    print(op(x, y))

math(lambda a,b: a*b, 2, 3)