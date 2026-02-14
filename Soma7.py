while True:
    try:
        numeros = input()
        i = 0
        while(numeros[i] != '0'):
            soma = soma + int(numeros[i])
            i = i + 1
        
        print(soma)
    except EOFError:
        break