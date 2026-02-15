#Calculo de aprovação com exame

entrada = input() 
mediaFinal = float(entrada.split()[0]) 
qtFaltas = int(entrada.split()[1]) 
if(mediaFinal >= 6.0 and qtFaltas <= 30):
    print("Aprovado!") 
elif(mediaFinal >= 4.0 and qtFaltas <= 30): 
    print("Exame Final!")
else: 
    print("Reprovado!")