# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def Truth ():
    result = 0
    for n in range(0, 10):
        num = bin(n)
        num = num.replace('b', '0')
        X = int(num[-2])
        Y = int(num[-3])
        Z = int(num[-1])
        left_part = not(X or Y or Z)
        right_part = (not X) and (not Y) and (not Z)
        if left_part == right_part:
            result += 1
        print(X, Y, Z, left_part, right_part, left_part == right_part, result)
    print()
    if result == 10:
        return print(True)
    else:
        return print(False)

Truth()