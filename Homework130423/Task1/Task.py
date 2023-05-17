def giveASum(a) -> int:
    i = 0
    while (a > 0):
        i += a % 10
        a = a // 10
    return i


class NotANumber (Exception):
    def __init__(self):
        self.message = 'Вы ввели не число'

    def __str__(self) -> str:
        return self.message


class NotThreeDigits (Exception):
    def __init__(self):
        self.message = 'Вы ввели не трехзначное число'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input('Введите число:')
        if not a.isnumeric():
            raise NotANumber
        if int(a) >= 1000 or int(a) < 100:
            raise NotThreeDigits
        print(giveASum(int(a)))
    except NotANumber:
        print(NotANumber())
        main()
    except NotThreeDigits:
        print(NotThreeDigits())
        main()


main()
