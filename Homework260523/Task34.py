trans_table = str.maketrans({ord(i): None for i in 'йцкнгшщзхфвпрлджчсмтб'})


class NoVowels (Exception):
    def __init__(self) -> None:
        self.message = 'В фразе нет гласных'

    def __str__(self) -> str:
        return self.message


def countVowels(a: str) -> int:
    return len(a.translate(trans_table))


def isPoem(poem: list) -> bool:
    try:
        count = [x for x in map(countVowels, poem)]
        if 0 in count:
            raise NoVowels
        a = count[0]
        for b in count:
            if b != a:
                return False
        return True
    except IndexError:
        print(IndexError('В стихотворении не может быть пустой фразы'))
        main()


def main() -> None:
    try:
        poem = input('Какое стихотворение придумал Винни? ').replace(
            '-', '').split()
        if isPoem(poem):
            print('Парам пам-пам')
        else:
            print('Пам парам')
    except ValueError:
        print(ValueError('Что-то не так со вводом'))
        main()
    except NoVowels:
        print(NoVowels())
        main()


main()
