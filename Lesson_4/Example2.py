list1 = [1,2,3,5,8,15,23,38]

# def select(f, col):           Это чистый map
#     return [f(x) for x in col]

# def where(f, col):           Это чистый filter
#     return [x for x in col if f(x)]

print([(x, x**2) for x in filter(lambda x: x % 2 == 0, map(int, list(input('Введите числа через пробел').split())))])