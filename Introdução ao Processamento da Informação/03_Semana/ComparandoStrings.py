while True:
    try:
        # Lê a linha e divide em uma lista de strings
        linha = input().split()
            
        # Atribui as duas strings conforme a entrada
        s1 = linha[0]
        s2 = linha[1]
        
        # Compara as strings e imprime o resultado
        if s1 == s2:
            print("iguais")
        else:
            print("diferentes")
            
    except EOFError:
        # Encerra o programa ao chegar no final do arquivo [cite: 23]
        break
