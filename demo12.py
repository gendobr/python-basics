# List Comprehension
d = [
    1,
    2,
    3,
    4,
    5,
    10,
]

d2 = [x * 2 for x in d]
"""
d2 = list()
for x in d:
   d2.append(x*2)
"""
print(d2)


d2tuple = tuple(x * 2 for x in d)
print(d2tuple)

d2set = {x * 2 for x in d}
print(d2set)

d2dict = {x: x * 2 for x in d}
print(d2dict)
print(d2dict[10])


print([x * 2 for x in d if x % 2 == 1])
