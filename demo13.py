"""
Лабораторна робота 7
Хто виконав:
Завдання:
13. Напишіть функцію Python, яка приймає число як параметр і перевіряє, 
чи число є простим чи ні. Примітка: просте число 
— це натуральне число, більше за 1 і яке не має додатних дільників, 
крім 1 і самого себе.
"""


def is_prime(x: int) -> bool:
    n = 0
    for d in range(1, x + 1):
        if x % d == 0:
            n = n + 1
    return n == 2


num = int(input("Надрукуйте натуральне число: "))
d = is_prime(num)
print(num, d)


"""
Результат

$ python demo13.py 
2 True
3 True
4 False
5 True

"""
