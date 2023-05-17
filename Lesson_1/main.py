def isPalyndrome(a):
    return a == a[::-1]


class NotANumber (Exception):
    def __init__(self):
        self.message = 'Вы ввели не число'

    def __str__(self) -> str:
        return self.message


def main():
    try:
        a = input('Введите цифры из билета:')
        if not a.isnumeric():
            raise NotANumber
        print(isPalyndrome(a))
    except NotANumber:
        print(NotANumber())
        main()


main()
