while true:
    try:
        numeros = input()
        i = 0
        while(numero[i] != '0'):
            soma = soma + int(numero[i])
            i = i + 1
        
        print(soma)
    except EOFError:
        break