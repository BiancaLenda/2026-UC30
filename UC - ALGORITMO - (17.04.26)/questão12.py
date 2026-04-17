while True:
    print("menu da calculadora")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicacao")
    print("4 - divisão")
    print("5 - sair")

    try:
        opcao = int(input("escolha uma opção: "))

        if opcao == 5:
            print("saindo")
            break

        n1 = float(input("digite o primeiro numero: "))
        n2 = float(input("digite o segundo numero: "))

        if opcao == 1:
            print("resultado:", n1 + n2)
        elif opcao == 2:
            print("resultado:", n1 - n2)
        elif opcao == 3:
            print("resultado:", n1 * n2)
        elif opcao == 4:
            if n2 != 0:
                print("resultado:", n1 / n2)
            else:
                print("erro: não pode dividir por zero")
        else:
            print("opcao não existe")

    except:
        print("erro: digite apenas números")

