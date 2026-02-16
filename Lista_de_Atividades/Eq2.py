from math import sqrt
coeficientes = input()
a = float(coeficientes.split()[0])
b = float(coeficientes.split()[1])
c = float(coeficientes.split()[2])
delta = pow(b, 2.0) - 4.0 * a * c
x1 = (-b + sqrt(delta)) / (2.0 * a)
x2 = (-b - sqrt(delta)) / (2.0 * a)

print("%.4f %.4f" %(x1, x2))
