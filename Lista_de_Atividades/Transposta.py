entrada = input().split()
while len(entrada) < 2:
    entrada += input().split()
n = int(entrada[0])
m = int(entrada[1])

# Carrega todos os elementos em uma lista linear para facilitar o acesso
elementos = []
while len(elementos) < n * m:
    linha = input().split()
    for e in linha:
        elementos.append(e)

# Constrói a transposta acessando os elementos por coluna
for j in range(m):
    linha_transposta = []
    for i in range(n):
        # O elemento D[i][j] na lista linear está em (i * m + j)
        linha_transposta.append(elementos[i * m + j])
    
    # Imprime a linha sem espaço no final
    print(" ".join(linha_transposta))