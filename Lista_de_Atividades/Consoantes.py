#Conta a quantidade de consoantes recebidas e mostra o total quando recebe o *.

letra = input().rstrip();
qtConsoantes = 0;
while(letra != "*"):
    if(letra.upper() != 'A' and letra.upper() != 'E' and letra.upper() != 'I' and letra.upper() != 'O' and letra.upper() != 'U'):
        qtConsoantes = qtConsoantes + 1;
    letra = input().rstrip();

print(qtConsoantes)