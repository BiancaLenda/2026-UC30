valor_compra = float(input("digite o valor da compra: "))

if valor_compra < 100:
    desconto = 0

elif valor_compra >= 100 and valor_compra < 500:
    desconto = valor_compra * 0.05

elif valor_compra >= 500 and valor_compra < 1000:
    desconto = valor_compra * 0.10

else:
    desconto = valor_compra * 0.15

valor_final = valor_compra - desconto

print("\nvalor original da compra: r$", valor_compra)
print("desconto aplicado: r$", desconto)
print("valor final a pagar: r$", valor_final)
