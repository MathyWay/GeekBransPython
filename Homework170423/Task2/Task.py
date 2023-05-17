from math import sqrt

def giveNumbers(a, b) -> tuple:
    return (((a + sqrt(a*a - 4*b)) / 2), ((a - sqrt(a*a - 4*b)) / 2))


class NotCorrectInput(Exception):

    def __init__(self):
        self.message = 'Что-то не так со вводом, перепроверьте'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input(
            'Введите два числа от Пети:'
        )
        a = a.replace(' ', '').split(',')
        while '' in a:
            a.remove('')
        if len(a) != 2:
            raise NotCorrectInput
        b = giveNumbers(int(a[0]), int(a[1]))
        for item in b:
            if item != int(item):
                raise NotCorrectInput
        print('Загаданные петей числа:{}, {}'.format(*b))

    except NotCorrectInput:
        print(NotCorrectInput())
        main()

    except ValueError:
        print(ValueError('Где-то закралось не число'))
        main()


main()