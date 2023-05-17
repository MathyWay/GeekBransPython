class NotCorrectArrLength(Exception):

    def __init__(self):
        self.message = 'Что-то не так с количеством элементов в массиве'

    def __str__(self) -> str:
        return self.message


def giveClosestNumber(a: list, n: int) -> int:
    ret = a[0]
    diverg = abs(n - ret)
    for i in a:
        if abs(i - n) < diverg:
            ret = i
            diverg = abs(i - n)
    return ret


def main() -> None:
    try:
        n = int(input(
            'Введите количество элементов в массиве: '
        ))
        a = input(
            'Введите массив чисел через пробел: '
        )
        a = a.split(' ')
        while '' in a:
            a.remove('')
        a = [int(i) for i in a]
        if len(a) != n or len(a) == 0:
            raise NotCorrectArrLength
        x = int(input(
            'Введите число, близость к которому будет анализироваться: '
        ))
        print(giveClosestNumber(a, x))

    except NotCorrectArrLength:
        print(NotCorrectArrLength())
        main()

    except ValueError:
        print(ValueError('Где-то закралось не число'))
        main()


main()
