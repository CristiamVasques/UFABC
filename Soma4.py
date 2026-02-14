#Receba N sequencias de M números inteiros e realize a soma desses valores

N = int(input())
for i in range(0, N, 1):
    M = int(input())
    soma = 0
    for j in range(0, M, 1):
        num = int(input())
        soma = soma + num
    print(soma)
