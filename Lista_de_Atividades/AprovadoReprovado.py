#Calculo de aprovação e reprovação

entrada = input() 
mediaFinal = float(entrada.split()[0]) 
qtFaltas = int(entrada.split()[1]) 

if(mediaFinal >= 6.0 and qtFaltas <= 30):
    print("Aprovado!")
else: 
    print("Reprovado!")