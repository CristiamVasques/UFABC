while True:
    try:
        # Lê a linha da entrada padrão
        linha = input().strip()
        
        # Ignora linhas vazias se houver
        if not linha:
            continue
            
        contador_pares = 0
        
        # Itera por cada dígito (caractere) da string lida
        for digito in linha:
            # Converte o caractere para inteiro e verifica se é par
            if int(digito) % 2 == 0:
                contador_pares += 1
        
        # Exibe a quantidade de dígitos pares [cite: 12]
        print(contador_pares)
        
    except EOFError:
        # Encerra o loop quando atingir o fim da entrada 
        break