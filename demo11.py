
# список
# https://www.w3schools.com/python/python_lists.asp
d = ["a", "b", "c", "d", "e", "f", "g"]
#     0    1    2    3    4    5    6

print(d[2])

d.append("h")
# ["a", "b", "c", "d", "e", "f", "g"]
#   0    1    2    3    4    5    6
d.remove("b")
# ["a", "c", "d", "e", "f", "g"]
#   0    1    2    3    4    5 

print(d)
print(d[7])

d[2] = "C"
print(d[2])

# кортеж
# https://www.w3schools.com/python/python_tuples.asp
# U = ("a", "b", "c", "d", "e", "f", "g")
U = tuple(d)
print(U[2])
# U[2] = "C"

for x in U:
	print("========" + x)


# множина
# set
# https://www.w3schools.com/python/python_sets.asp
S = {"a", "b", "a"}
print(S)
S.add("")

S = {"a", "c", "b"}
print(S)


# словник
# dictionary
# associative list
dct = {
	"a": "AAA",
	"b": "BBB",
	"c": "CCC",
	"d": "DDD",
}
print(dct["a"])
