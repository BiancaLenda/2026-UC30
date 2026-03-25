def calculadora(a,b):
  print("[1] adição")
  print("[2] subtração")
  print("[3] multiplicação")
  print("[4] divisão")
  print("[0] sair")
  opcao = int(input("digite sua opção: "))
  match opcao: 
    case 1:
      return a + b
    case 2:
      return  a - b
    case 3:
      return a * b
    case 4:
      return  a / b
    case 0:
      print("saindo...")
    case _:
      print("opção inválida")


  
