def somaVet(v, tam):
    soma = 0
    for i in range(0, tam, 1):
        soma = soma + v[i]
    return soma

n = int(input())
vet = [0] * n
entrada = input().split()
for i in range(0, n, 1):
    vet[i] = int(entrada[i])
print(somaVet(vet, n))
