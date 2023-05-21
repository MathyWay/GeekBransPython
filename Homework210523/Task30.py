def main() -> None:
    try:
        a1 = int(input('Введите первый элемент последовательности'))
        div = int(input('Введите разность/шаг последовательности'))
        n = int(input('Введите количество элементов последовательности'))
        print([a1 + x for x in map(lambda x: div*x, range(0, n))])
    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()


main()
