#Recebe uma sequencia de números inteiros em linha e realiza a soma desses valores.

Soma = 0
Numeros = input().split()
for i in range(0, len(Numeros)-1, 1):
    Soma = Soma + int(Numeros[i])

print(Soma)
