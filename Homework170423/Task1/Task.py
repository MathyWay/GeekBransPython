def giveHowMuchCoins(a) -> int:
    summa = 0
    for i in a:
        summa += int(i)
    summa = float(summa) / len(a)
    if summa > 0.5:
        return round((1 - summa) * len(a))
    else:
        return round(summa * len(a))


class NotCorrectNumber(Exception):

    def __init__(self):
        self.message = 'Вы ввели не только 0 и 1'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input(
            'Введите расположение монеток в ряду через запятую: 0 - орёл, 1 - решка:'
        )
        a = a.replace(' ', '').split(',')
        while '' in a:
            a.remove('')
        for smth in a:
            if int(smth) > 1 or int(smth) < 0:
                raise NotCorrectNumber
        print('Нужно будет перевернуть:{}'.format(giveHowMuchCoins(a)))

    except NotCorrectNumber:
        print(NotCorrectNumber())
        main()

    except ValueError:
        print(ValueError('Где-то закралось не число'))
        main()


main()
