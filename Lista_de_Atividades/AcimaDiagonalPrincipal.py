# Leitura da operação (S ou M) e do tamanho N
try:
    # Captura a operação
    entrada_op = input().split()
    while not entrada_op:
        entrada_op = input().split()
    operacao = entrada_op[0]

    # Captura a dimensão N
    entrada_n = input().split()
    while not entrada_n:
        entrada_n = input().split()
    n = int(entrada_n[0])

    soma_area = 0.0
    contagem_elementos = 0
    
    # Processamento linha por linha
    for i in range(n):
        valores_linha = []
        # Garante a leitura de N elementos para a linha atual
        while len(valores_linha) < n:
            linha_input = input().split()
            for v in linha_input:
                valores_linha.append(v)
        
        # Elementos acima da diagonal principal: coluna (j) > linha (i)
        for j in range(i + 1, n):
            soma_area += float(valores_linha[j])
            contagem_elementos += 1

    # Cálculo do resultado final
    if operacao == 'S':
        resultado = soma_area
    else:
        # Média: soma dividida pela quantidade de elementos acima da diagonal
        resultado = soma_area / contagem_elementos

    # Saída formatada com uma casa decimal 
    print(f"{resultado:.1f}")

except EOFError:
    pass