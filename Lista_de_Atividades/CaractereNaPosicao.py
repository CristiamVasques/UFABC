""""Receba uma string e um inteiro e retorne o caractere que está na posição da string correspondente 
ao inteiro informado."""

entrada = input()
       
# Divide a string pelo espaço
partes = entrada.split()
        
# Verifica se temos os dois componentes: S e P
if len(partes) == 2:
    s = partes[0]      # A string S 
    p = int(partes[1]) # A posição P 
            
# Imprime o caractere na posição P e salta uma linha 
print(s[p])
