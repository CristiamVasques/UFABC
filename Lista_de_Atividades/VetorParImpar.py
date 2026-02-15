def vetorParImpar(v, n):
    for i in range(0, n, 1):
        if(v[i] % 2 == 0):
            v[i] = 0
        else:
            v[i] = 1

MAX_TAMANHO = 100
vetor = [0] * MAX_TAMANHO
n = int(input())
while(n != 0):
    linha = input().split()
    for i in range(0, n, 1):
        vetor[i] = int(linha[i])

    vetorParImpar(vetor, n)

    for i in range(0, n, 1):
        print(str(vetor[i]) + (" " if i < n-1 else "\n"), end="")

    n = int(input())