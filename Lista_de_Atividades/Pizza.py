Alunos = int(input())
FatiasPizzaGrande = 8
FatiasPizzaMedia = 6
QtddG = int(input()) * FatiasPizzaGrande
QtddM = int(input()) * FatiasPizzaMedia

PizzaTotal = QtddG + QtddM
SobraPizza = PizzaTotal - Alunos

if SobraPizza <= 0:
    print(0)
else:
    print(SobraPizza)