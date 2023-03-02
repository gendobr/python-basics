def is_prime(x: int) -> bool:
    n = 0
    for d in range(1, x + 1):
        if x % d == 0:
            n = n + 1
    return n == 2


def multiply(x: int, y: int, z: int) -> int:
    return x * y * z


# print(multiply(2, 3, 4))
# print(multiply(2, 3, 4))


def sum_all(*args) -> int:
    s = 0
    for x in args:
        s = s + x
    return s


print(sum_all(2, 3, 4, 5))


def multiply(x, y, z):
    return x * y * z


print(multiply(8, 3, "a"))
"""
multiply(x, y,  z )
multiply(8, 3, "a")
return 8 * 3 * "a"
"""


def calc_all(x, y) -> list:
    return [x + y, x * y]


print(calc_all(3, 7))


# closures / замикання
