receptor, doador = input().split()
if(receptor == "AB" or doador =="O" or receptor == doador):
    print("transfusao compativel")
else:
    print("transfusao incompativel")