
# Напишіть програму, яка друкує всі дільники заданого числа
z = 24

d = 1
while d <= 24:
    if z % d == 0:
   		print(d)
    d = d + 1

print('=====')
for d in range(1, 25):
    if z % d == 0:
   		print(d)
