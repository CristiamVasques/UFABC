#Vetores de tamanho fixo na declaração: 
#Eventual mal gerenciamento do espaço alocado provocará erro em tempo de execução (runtime error).

TAMANHO = 100
idades = [0] * TAMANHO
alturas = [0.0] * TAMANHO
pesos = [0.0] * TAMANHO
generos = [''] * TAMANHO
qtdMasc = 0
qtdFem = 0
qtdMascAcimaAlt = 0
qtdFemAbaixoPeso = 0
somaAltMasc = 0
somaPesoFem = 0

for i in range(0, TAMANHO, 1):
    print("Informe a idade do " + str(i+1) + "o. atleta: ", end="")
    idades[i] = int(input())
    print("Informe a altura do " + str(i+1) + "o. atleta: ", end="")
    alturas[i] = float(input())
    print("Informe a peso do " + str(i+1) + "o. atleta: ", end="")
    pesos[i] = float(input())
    print("Informe a genero do " + str(i+1) + "o. atleta: ", end="")
    generos[i] = input()

    if(generos[i] == 'M'):
        somaAltMasc = somaAltMasc + alturas[i]
        qtdMasc = qtdMasc + 1
    else:
        somaPesoFem = somaPesoFem + pesos[i]
        qtdFem = qtdFem + 1

for i in range(0, TAMANHO, 1):
    if(qtdMasc != 0 and alturas[i] > (somaAltMasc/qtdMasc) and generos[i] == 'M'):
        qtdMascAcimaAlt = qtdMascAcimaAlt + 1

    if(qtdFem != 0 and pesos[i] < (somaPesoFem/qtdFem) and generos[i] == 'F'):
        qtdFemAbaixoPeso = qtdFemAbaixoPeso + 1

if(qtdMasc != 0):
    print("Ha " + str(qtdMascAcimaAlt) + " atletas homens acima da media da altura dos homens.")
else:
    print("Nao houve entrada de atletas homens.")

if(qtdFem != 0):
    print("Ha " + str(qtdMascAcimaAlt) + " atletas mulheres abaixo da media do peso das mulheres.")
else:
    print("Nao houve entrada de atletas mulheres.")