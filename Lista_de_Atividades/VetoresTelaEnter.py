tamanho = 10
vet = [0] * tamanho
for i in range(0, tamanho, 1):
    if i < tamanho - 1:
        print(vet[i], end=" ")
    else:
        print(vet[i], end="\n")