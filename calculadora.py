while True:
    
    primeiro_numero = int(input("digite o primeiro numero: "))
    
    while True:
        operacao = int(input("qual operacao deseja fazer? 1 = +, 2 = -, 3 = *, 4 = /: "))
        
        if operacao <= 4 and operacao >= 1:
            break
        else:
            print("operaçao invalida...")
            pass
        
    segundo_numero = int(input("digite o segundo numero: "))
        
    if operacao == 1:
        print(primeiro_numero + segundo_numero)
    elif operacao == 2:
        print(primeiro_numero - segundo_numero)
    elif operacao == 3:
        print(primeiro_numero * segundo_numero)
    else:
        print(primeiro_numero / segundo_numero)
    
    a = input("deseja continuar? 0- nao: ")
    if a == "0":
        break
    else:
        pass
        
        