data = '15 156 96 3 5 8 52 9'
print(list(map(int, data.split())))
res = list(filter(lambda x: x % 10 == 5, list(map(int, data.split()))))
print(res)