def seu_imc():
    try:
        peso = float(input("digite seu peso (kg): "))
        altura = float(input("digite sua altura (m): "))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("seu índice de massa corporal é:", imc, "categoria: magro")
        elif imc <= 24.9:
            print("seu índice de massa corporal é:", imc, "categoria: normal")
        elif imc <= 29.9:
            print("seu índice de massa corporal é:", imc, "categoria: sobrepeso")
        else:
            print("seu índice de massa corporal é:", imc, "categoria: obesidade")

    except:
        print("entrada inválida, digite apenas números!")

seu_imc()