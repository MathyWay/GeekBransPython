book = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}


def giveScramble(a: str) -> int:
    ret = 0
    a = a.upper()
    for i in a:
        ret += book[i]
    return ret


def main() -> None:
    try:
        count = 0
        n = str(input(
            'Введите слово: '
        ))
        print(giveScramble(n))

    except TypeError:
        print(TypeError('Что-то не так со вводом'))
        main()


main()
