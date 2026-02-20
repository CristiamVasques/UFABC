# Leitura de N (Norte-Sul) e M (Leste-Oeste)
entrada = input().split()
while not entrada:
    entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])

# Inicializa uma lista para armazenar a soma de cada uma das M avenidas
somas_avenidas = [0] * m

# Processa N fileiras de quadras
for _ in range(n):
    valores_fileira = []
    while len(valores_fileira) < m:
        linha = input().split()
        for v in linha:
            valores_fileira.append(int(v))
    
    # Soma o valor de cada quadra à sua respectiva avenida (coluna)
    for j in range(m):
        somas_avenidas[j] += valores_fileira[j]

# Encontra o menor valor entre todas as somas calculadas
menor_valor = somas_avenidas[0]
for soma in somas_avenidas:
    if soma < menor_valor:
        menor_valor = soma

print(menor_valor)