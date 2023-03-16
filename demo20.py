txt = "Створіть рядок"  # UTF8 / UTF16
x = txt.encode("utf-8")
print(x)

y = b"\xd0\xa1\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd1\x96\xd1\x82\xd1\x8c \xd1\x80\xd1\x8f\xd0\xb4\xd0\xbe\xd0\xba"
z = y.decode("utf-8")
print(z)

print(y.decode("windows-1251"))
# print(y.decode("windows-1252"))


txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

"""
"Hello,  John welcome  to my world."
"""
print(txt.replace("welcome", " John welcome "))

for c in txt:
    print(c, c.islower())
