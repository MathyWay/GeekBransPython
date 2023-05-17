class NotCorrectArrLength(Exception):

    def __init__(self):
        self.message = 'Что-то не так с количеством элементов в массиве'

    def __str__(self) -> str:
        return self.message


def giveCount(a: list, n: int) -> int:
    ret = 0
    for i in a:
        if int(i) == n:
            ret += 1
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
        if len(a) != n:
            raise NotCorrectArrLength
        x = int(input(
            'Введите число, встречаемость которого будет анализироваться: '
        ))
        print(giveCount(a, x))

    except NotCorrectArrLength:
        print(NotCorrectArrLength())
        main()

    except ValueError:
        print(ValueError('Где-то закралось не число'))
        main()


main()
