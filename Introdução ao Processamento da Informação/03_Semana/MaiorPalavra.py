#Identifica a maior palavra

maiorStr = "";
primeira = True;
while True:
    try:
        str = input();
        if(primeira or len(str) > len(maiorStr)):
            maiorStr = str;
            primeira = False;
    except EOFError:
        if(not primeira):
            print("A maior palavra informada foi " + maiorStr);
        else:
            print("Nenhuma palavra foi informada");
        break;