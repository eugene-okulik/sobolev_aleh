import math

a, b = map(float, input("enter a b: ").split())

hypot = math.sqrt(a**2 + b**2)
S = 0.5 * a * b

print(f"hypot = {round(hypot, 1)}")
print(f"S = {round(S, 1)}")
