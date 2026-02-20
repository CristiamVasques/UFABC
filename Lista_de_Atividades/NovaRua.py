entrada = input().split()
while not entrada:
    entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])

menor_valor_rua = -1

for _ in range(n):
    valores_fileira = []
    while len(valores_fileira) < m:
        linha = input().split()
        for v in linha:
            valores_fileira.append(int(v))
    
    # Calcula a soma da rua atual
    soma_atual = 0
    for valor in valores_fileira:
        soma_atual += valor
        
    # Verifica se é a menor soma encontrada até agora
    if menor_valor_rua == -1 or soma_atual < menor_valor_rua:
        menor_valor_rua = soma_atual

print(menor_valor_rua)