def main() -> None:
    try:
        col = list(map(int, list(input('Введите числа через пробел ').split())))
        minn = int(input('Введите нижнюю границу '))
        maxx = int(input('Введите верхнюю границу '))
        print([x for x in filter(lambda x: col[x] > minn and col[x] < maxx, range(0, len(col)))])
    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()


main()