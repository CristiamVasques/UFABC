while True:
    try:
        nomicula = input().strip() # 
        if not nomicula:
            continue
            
        nome = ""
        matricula = ""
        
        for char in nomicula:
            if '0' <= char <= '9':
                matricula += char
            else:
                nome += char
        
        print(nome + " " + matricula)
        
    except EOFError:
        break