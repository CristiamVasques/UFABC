# Leitura do tamanho do vetor N
entrada_n = input().split()
while not entrada_n:
    entrada_n = input().split()
n = int(entrada_n[0])

# Leitura dos N elementos do vetor V
v = []
while len(v) < n:
    linha_v = input().split()
    for item in linha_v:
        v.append(int(item))

# Leitura da quantidade de buscas M
entrada_m = input().split()
while not entrada_m:
    entrada_m = input().split()
m = int(entrada_m[0])

# Processamento de cada uma das M buscas
buscas_realizadas = 0
while buscas_realizadas < m:
    entrada_busca = input().split()
    if not entrada_busca:
        continue
    
    for x_str in entrada_busca:
        if buscas_realizadas >= m:
            break
            
        x = int(x_str)
        indice_encontrado = -1
        
        # Busca sequencial para encontrar a primeira ocorrência
        for i in range(n):
            if v[i] == x:
                indice_encontrado = i
                break # Interrompe no primeiro índice encontrado
        
        # Saída do resultado seguido de uma linha em branco
        print(indice_encontrado)
        buscas_realizadas += 1