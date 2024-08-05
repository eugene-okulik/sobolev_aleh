import math

a = float(input("a = "))
b = float(input("b = "))

a_middle = (a + b) / 2
g_middle = math.sqrt(a * b)

print("a_middle = ", round(a_middle, 4))
print("g_middle = ", round(g_middle, 4))
