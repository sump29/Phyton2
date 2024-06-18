import math

def L(x, y, z):
    return (math.sqrt(x**2 + z**2 + math.cos(z*x)**2) + math.sqrt(y**2 + x**2 + math.cos(x*y)**2)) / math.sqrt(z**2 + y**2 + math.cos(z*y)**3)

x = 1
y = 1
z = 1

print(L(x, y, z))