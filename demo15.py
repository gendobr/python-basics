def calc_all(x, y) -> list:
    z = 4  # ЛОКАЛЬНІ ЗМІННІ
    return [z * (x + y), z * x * y]


print(calc_all(3, 7))
# print(z)


# closures / замикання
def calc_2(x, y) -> list:
    return [S * (x + y), S * x * y]


S = 4  # ГЛОБАЛЬНІ ЗМІННІ
print(calc_2(3, 7))

S = 5
print(calc_2(3, 7))


# closures / замикання
def calc_3(x, y) -> list:
    global S
    S = S - 1
    return [S * (x + y), S * x * y]


print(calc_3(3, 7))

print(calc_3(3, 7))
