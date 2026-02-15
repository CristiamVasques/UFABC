somaNotas = 0 
contador = 0 
while(contador < 10): 
    nota = float(input("Informe a " + str(contador + 1) + "a. nota:\n")) 
    somaNotas = somaNotas + nota 
    contador = contador + 1 
mediaFinal = somaNotas / 10. 
        
print("Sua Media Final dos Trabalhos (NFT) foi %.2f" %mediaFinal)