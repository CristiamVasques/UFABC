N = int(input())
valores = list(map(int, input().split()))
menor = valores[0]
posicao = 0
for i in range(1, N):
    if valores[i] < menor:
        menor = valores[i]
        posicao = i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")