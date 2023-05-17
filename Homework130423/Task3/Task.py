def isLucky(a) -> bool:
    sum = 0
    for i in range(0, 3):
        sum += int(a[i]) - int(a[len(a) - i - 1])
    # Не, ну можно конечно (int(a[0]) + int(a[1]) + int(a[2]) - int(a[3]) - int(a[4]) - int(a[5])) == 0,
    # но это как-то не по-божески
    return sum == 0


class NotANumber (Exception):
    def __init__(self):
        self.message = 'Вы ввели не число'

    def __str__(self) -> str:
        return self.message


class NotSixDigit (Exception):
    def __init__(self):
        self.message = 'Билет у вас паленый, не то количество цифр, сэр'

    def __str__(self) -> str:
        return self.message


def main() -> None:
    try:
        a = input('Введите номер билета:')
        if not a.isnumeric():
            raise NotANumber
        if int(a) >= 1000000 or int(a) <= 100000:
            raise NotSixDigit
        print(isLucky(a))
    except NotANumber:
        print(NotANumber())
        main()
    except NotSixDigit:
        print(NotSixDigit())
        main()


main()
