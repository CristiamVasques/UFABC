# Leitura inicial de q1 e q2 da entrada padrão
# Nota: O uso de input().split() é o padrão nativo do Python
entrada_config = input().split()
while len(entrada_config) < 2:
    entrada_config += input().split()

q1 = int(entrada_config[0])
q2 = int(entrada_config[1])

# Coleta dos valores para v1
v1 = []
while len(v1) < q1:
    linha = input().split()
    for item in linha:
        v1.append(int(item))

# Coleta dos valores para v2
v2 = []
while len(v2) < q2:
    linha = input().split()
    for item in linha:
        v2.append(int(item))

# Inicialização do processo de intercalação (Merge)
vr = []
i = 0  # Índice para v1
j = 0  # Índice para v2

# Intercalação comparativa enquanto houver elementos em ambos os vetores
while i < q1 and j < q2:
    if v1[i] <= v2[j]:
        vr.append(v1[i])
        i += 1
    else:
        vr.append(v2[j])
        j += 1

# Adiciona os elementos restantes, se houver, de v1
while i < q1:
    vr.append(v1[i])
    i += 1

# Adiciona os elementos restantes, se houver, de v2
while j < q2:
    vr.append(v2[j])
    j += 1

# Impressão do resultado final de forma crescente
for valor in vr:
    print(valor)