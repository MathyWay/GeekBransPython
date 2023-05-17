import  random

def giveList(length : int) -> list:
    return [int(random.randint(0, 10)) for i in range(length)]

def giveIntersec(a : list, b : list) -> list:
    ret = list(set(a)&set(b))
    ret.sort()
    return ret

def main() -> None:
    try:
        a = 0
        b = 0
        a = int(input(
            'Введите число a: '
        ))
        b = int(input(
            'Введите число b: '
        ))
        c = giveList(a)
        d = giveList(b)
        print(c)
        print(d)
        print(giveIntersec(c, d))

    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()


main()