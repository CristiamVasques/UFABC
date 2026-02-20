try:
    n_entrada = input().split()
    while not n_entrada:
        n_entrada = input().split()
    n = int(n_entrada[0])

    eh_triangular_superior = True
    for i in range(n):
        valores_linha = []
        while len(valores_linha) < n:
            linha = input().split()
            for v in linha:
                valores_linha.append(int(v))
        
        # Verifica elementos abaixo da diagonal principal na linha atual
        for j in range(i):
            if valores_linha[j] != 0:
                eh_triangular_superior = False
                break
                
    if eh_triangular_superior:
        print("SIM")
    else:
        print("NAO")
except EOFError:
    pass