a = int(input("сторона 1 "))
b = int(input("сторона 2 "))
c = int(input("сторона 3 "))

if (a+b > c) and (a + c > b) and (b +c > a):
	print("Трикутник існує")
else:
	print("Трикутник не існує")
