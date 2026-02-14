#Recebe dois números e calcula o primeiro elevado pelo segundo.

numeros = input()
A = int(numeros.split()[0])
N = int(numeros.split()[1])
Resultado = A ** N

print("%.4f" %Resultado)