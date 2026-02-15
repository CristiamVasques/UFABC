while True:
    try:
        # Recebe as strings
        entrada = input().split()
            
        # Armazena as strings recebidas
        string1 = entrada[0]
        string2 = entrada[1]
                
        # Imprime as strings concatenadas
        print(string1 + string2)
            
    except EOFError:
        # Encerra o programa ao chegar no final do arquivo [cite: 23]
        break