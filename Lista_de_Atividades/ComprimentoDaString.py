while True:
    try:
        # Recebe a string
        linha = input()
            
        # Conta a quantidade de caracteres
        comprimento = len(linha)
                
        # Imprime o comprimento da palavra
        print(comprimento)
            
    except EOFError:
        # Encerra o programa ao chegar no final do arquivo [cite: 23]
        break