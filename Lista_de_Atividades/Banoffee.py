Alunos = int(input())
FatiasBanoffeeGrande = 8
FatiasBanoffeeMedia = 6
QtddG = int(input()) * FatiasBanoffeeGrande
QtddM = int(input()) * FatiasBanoffeeMedia

BanoffeeTotal = QtddG + QtddM
SobraBanoffee = BanoffeeTotal - Alunos

if SobraBanoffee <= 0:
    print(0)
else:
    print(SobraBanoffee)