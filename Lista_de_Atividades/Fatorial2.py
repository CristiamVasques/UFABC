while True:
    try:
        # Lê a entrada N
        line = input()
        if not line:
            break
        n = int(line)
        
        # Condição de parada: N negativo 
        if n < 0:
            break
            
        # Cálculo do fatorial
        # O Python lida nativamente com números grandes, como 20! 
        fat = 1
        for i in range(1, n + 1):
            fat = fat * i
            
        # Imprime o resultado e salta uma linha após cada impressão
        print(fat)
        
    except EOFError:
        break