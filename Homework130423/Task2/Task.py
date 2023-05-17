def giveAnAnswer(a) -> tuple:
    return (a/6, a/6, 2*a/3)


class NotANumber (Exception):
    def __init__(self):
        self.message = 'Вы ввели не число'

    def __str__(self) -> str:
        return self.message


class NotDivSix (Exception):
    def __init__(self):
        self.message = 'Какие-то обрубленные у вас журавлики такого быть не может'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input('Введите число:')
        if not a.isnumeric():
            raise NotANumber
        if int(a) % 6 != 0:
            raise NotDivSix
        print(giveAnAnswer(int(a)))
    except NotANumber:
        print(NotANumber())
        main()
    except NotDivSix:
        print(NotDivSix())
        main()


main()
