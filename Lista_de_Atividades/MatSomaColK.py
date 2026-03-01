n, k = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

coluna_index = k

coluna_soma = 0
for i in range(n):
    coluna_soma += matrix[i][coluna_index]

print(coluna_soma)