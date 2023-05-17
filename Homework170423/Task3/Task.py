from math import pow, log

def giveNumbers(a) -> object:
    return (pow(2, i) for i in range(1, int(log(a, 2)) + 1))


def main() -> None:
    try:
        a = int(input(
            'Введите число:'
        ))
        if(a >= 2):
            print('Степени двойки меншье числа {}:'.format(a), *giveNumbers(a))
        else:
            print('Нет таких чисел')

    except ValueError:
        print(ValueError('Где-то закралось не число'))
        main()


main()