total = 0.0
valor = float(input("digite o valor do item desejado ou 0 para encerrar a compra: "))

while valor != 0:
    total += valor
    valor = float(input("digite o valor do próximo item ou 0 para encerrar a compra: "))

print("O total da compra é:", total)