# Leitura da operação e do tamanho N
try:
    # Captura a operação (S para soma ou M para média)
    entrada_op = input().split()
    while not entrada_op:
        entrada_op = input().split()
    operacao = entrada_op[0]

    # Captura a dimensão N da matriz (2 < N <= 1000)
    entrada_n = input().split()
    while not entrada_n:
        entrada_n = input().split()
    n = int(entrada_n[0])

    soma_abaixo = 0.0
    total_elementos = 0
    
    # Processamento linha por linha para otimizar memória
    for i in range(n):
        valores_linha = []
        # Garante a leitura de todos os N elementos da linha atual
        while len(valores_linha) < n:
            linha_input = input().split()
            if not linha_input:
                break
            for v in linha_input:
                valores_linha.append(v)
        
        # Elementos abaixo da diagonal principal: coluna (j) < linha (i)
        if len(valores_linha) == n:
            for j in range(0, i):
                soma_abaixo += float(valores_linha[j])
                total_elementos += 1

    # Definição do resultado com base na operação solicitada
    if operacao == 'S':
        resultado = soma_abaixo
    else:
        # Média dos elementos da área verde
        resultado = soma_abaixo / total_elementos

    # Saída formatada com uma casa decimal e salto de linha
    print(f"{resultado:.1f}")

except EOFError:
    pass