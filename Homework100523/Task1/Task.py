def givePow(a : int, b : int, i = 0) -> int:
    if i == b or i > b:
        return 1
    else:
        return a * givePow(a, b, i + 1)

def main() -> None:
    try:
        a = int(input('Введите число А: '))
        b = int(input('Введите число B: '))
        print(givePow(a, b))

    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()


main()