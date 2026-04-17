frase = input("digite uma frase: ")

vogais = "aeiou"
contador = 0

for letra in frase:
    if letra.lower() in vogais:
        contador += 1

print("a quantidade de vogais é: ", contador)
