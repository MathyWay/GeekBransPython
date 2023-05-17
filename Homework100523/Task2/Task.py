def giveSum(a : int, b : int, i = 0) -> int:
    if i == b:
        return a
    else:
        return giveSum(a + 1, b, i + 1)

def main() -> None:
    try:
        a = int(input('Введите число А: '))
        b = int(input('Введите число B: '))
        print(giveSum(max(a, b), min(a, b)))

    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()


main()