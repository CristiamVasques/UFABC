N = int(input())
valores = list(map(int, input().split()))
maior = valores[0]
posicao = 0
for i in range(1, N):
    if valores[i] > maior:
        maior = valores[i]
        posicao = i
print(f"Maior valor: {maior}")
print(f"Posicao: {posicao}")