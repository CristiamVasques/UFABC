try:
    n_entrada = input().split()
    while not n_entrada:
        n_entrada = input().split()
    n = int(n_entrada[0])

    tem_abaixo = False # Se houver algo != 0 em i > j
    tem_acima = False  # Se houver algo != 0 em i < j

    for i in range(n):
        valores_linha = []
        while len(valores_linha) < n:
            linha = input().split()
            for v in linha:
                valores_linha.append(int(v))
        
        for j in range(n):
            if i > j and valores_linha[j] != 0:
                tem_abaixo = True
            elif i < j and valores_linha[j] != 0:
                tem_acima = True

    # Lógica de decisão conforme o enunciado
    if not tem_abaixo and not tem_acima:
        print("SIM: DIAGONAL")
    elif not tem_abaixo:
        print("SIM: SUPERIOR")
    elif not tem_acima:
        print("SIM: INFERIOR")
    else:
        print("NAO")
except EOFError:
    pass