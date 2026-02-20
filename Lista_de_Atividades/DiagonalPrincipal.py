# Leitura da operação (S ou M)
try:
    linha_op = input().split()
    while not linha_op:
        linha_op = input().split()
    operacao = linha_op[0]

    # Leitura da dimensão N da matriz
    linha_n = input().split()
    while not linha_n:
        linha_n = input().split()
    n = int(linha_n[0])

    soma_diagonal = 0.0
    
    # Processamento linha por linha para evitar carregar a matriz inteira
    # A diagonal principal ocorre quando o índice da linha é igual ao da coluna
    for i in range(n):
        valores_linha = []
        while len(valores_linha) < n:
            # Captura os valores da linha i 
            linha_atual = input().split()
            for v in linha_atual:
                valores_linha.append(v)
        
        # Somamos apenas o elemento onde coluna == linha (índice i)
        soma_diagonal += float(valores_linha[i])

    # Cálculo final conforme a operação solicitada
    if operacao == 'S':
        resultado = soma_diagonal
    else:
        resultado = soma_diagonal / n

    # Saída formatada com uma casa decimal e salto de linha
    print(f"{resultado:.1f}")

except EOFError:
    pass