def isAbleToCrack(a, b, c) -> bool:
    return (c % a == 0 and a * b >= c) or (c % b == 0 and a * b >= c)


class NotANumber (Exception):
    def __init__(self):
        self.message = 'Вы ввели не число'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input('Введите количество долек по первой оси:')
        if not a.isnumeric():
            raise NotANumber
        b = input('Введите количество долек по ортогональной оси:')
        if not b.isnumeric():
            raise NotANumber
        c = input('Введите желаемое количество долек:')
        if not c.isnumeric():
            raise NotANumber
        print(isAbleToCrack(int(a), int(b), int(c)))
    except NotANumber:
        print(NotANumber())
        main()


main()
