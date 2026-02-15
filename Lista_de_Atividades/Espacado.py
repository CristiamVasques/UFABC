#Recebe um string e acrescenta espaços entre as letras.

while True:
    try:
        str = input();
        for i in range(0, len(str), 1):
            if(i < len(str)-1):
                print(str[i], end=" ");
            else:
                print(str[i]);

    except EOFError:
        break;
