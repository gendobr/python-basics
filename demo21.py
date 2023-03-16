#     What are strings in Python?
#     Creating a string
a = "abcdefghijklmnop"
#    0123456789  12
#              10  13
#               11  14
b = "sadasdasdsa ' \\ \n \t \b \x78 \oa0"
c = """ 
qrewr
wewe
"""
d = """ 
qrewr
wewe
"""
f = "фівапррр"
g = b"qweqwewqeqw\x34"
h = r"шшщшхзщшхзщшхз"

#     Accessing individual characters in a string
print(a[1])

#     String concatenation
print(a + f)
print(" **** ".join([a, b, f]))


#     String repetition
print(" **** " * 5)
print(5 * " **** ")

#     Common string methods
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

"""
"Hello,  John welcome  to my world."
"""
print(txt.replace("welcome", " John welcome "))

for c in txt:
    print(c, c.islower())


#     Understanding string indexing
#     Accessing specific characters using indexing
#     String slicing
#     Slicing with step values
#     Reverse slicing
a = "abcdefghijklmnop"
print(a[1])
print(a[1:4])
print(a[0:6:2])
print(a[-2])
print(a[::-1])

x = list(a)
x.reverse()
print("".join(x))

#     Formatting strings with placeholders
#     Using the format() method
#     F-strings
#     String interpolation
#     Common formatting options
k = 10
print(f"Value of k is {k}")

print("Value of k is {}".format(k))
print("Value of k is {} {}".format("AAAAAAAA", "DDDDDDDDDDD"))

print("Value of k is {:f} {}".format(2, 3.2))
print("values: %i, strings: %s  %f" % (2 + 2, "2+2", k))


#     Common string methods
#     Modifying strings using string methods
#     Replacing substrings in a string
print(a.replace("a", "A"))
print(a.removeprefix("a"))
print(a.removeprefix("B"))
print(a.removesuffix("p"))

#     String case conversion methods
print(a.lower())
print(a.upper())
print(a.swapcase())

#     Removing whitespace from strings
d = "  dfdsf   ffdf   fddfs "
D = "dfdsf ffdf fddfs"
print("|" + d.strip() + "|")

#     Splitting and joining strings
x = list(a)
print(x)

D = "Matching patterns using regular expressions"
print(D.split(" "))

#     Introduction to regular expressions
import re

#     Creating regular expressions in Python
#     Matching patterns using regular expressions
#     Capturing groups
#     Common regular expression patterns
print(d)
print(re.sub(" +", " ", d))
print(
    re.split("[- ,.]", "Matching patterns using regular-expressions.Capturing groups.")
)
print(
    re.findall("re|te", "Matching patterns using regular-expressions.Capturing groups.")
)

#     Reading text files

f = open("demo20.txt", "r")
txt = f.read()
print(txt)
f.close()

f = open("demo20.txt", "r")
lines = f.readlines()
print(lines)
f.close()

#     Writing to text files
f = open("demo21.txt", "w")
for x in lines:
    x = ">>>>>>>>>>>>" + x
    f.write(x)
f.close()

#     Appending to text files
f = open("demo21.txt", "a")
for x in lines:
    x = "%%%%%%%%%" + x
    f.write(x)
f.close()


#     Reading and writing CSV files
import csv

f = open("demo21.csv")
csv_lines = csv.reader(f, delimiter="\t")
for row in csv_lines:
    print(row)
f.close()
#     Reading and writing JSON files
#     Unicode and character encoding
#     Byte strings
#     Comparing strings
#     String searching algorithms
#     String manipulation libraries
