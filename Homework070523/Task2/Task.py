def giveUrozhay(a : list) -> int:
    max = a[0]
    for i in range(len(a) - 2):
        count = a[i] + a[i+1] + a[i+2]
        if max < count:
            max = count
    return max

def main() -> None:
    try:
        with open("GardenBed.txt", 'r') as f:
            line = [int(n) for n in f.read().split()]
            print(line)
            line.append(line[0])
            line.append(line[1])
            print(giveUrozhay(line))

    except ValueError:
        print(ValueError('Что-то не так со вводом'))
#        main()


main()