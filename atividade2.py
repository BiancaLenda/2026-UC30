nome = input("digite seu nome:")
def exibirmensagem(nome):
    print(f"olá, {nome}")

vh = float(input("Quanto você ganha por hora: "))
ht = float(input("Quantas horas você trabalha: "))

def calcularsalario(vh,nt):
    salario = vh * ht
    return salario

resultado = calcularsalario(vh,ht)

print(f"Você recebe um total de: {resultado}")
