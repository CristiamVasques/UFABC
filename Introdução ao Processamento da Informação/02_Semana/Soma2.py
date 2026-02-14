#Recebe a quantidade de números que serão digitados e em seguida a soma dos números informados.

N = int(input())

Soma = 0

for i in range(0, N, 1):
    Num = int(input())
    Soma = Soma + Num

print(Soma)
