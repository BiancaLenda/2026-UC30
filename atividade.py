nome = input("digite seu nome:")
def exibirmensagem(nome):
    print(f"olá, {nome}")

n1 = float(input("digite um número: "))
n2 = float(input("digite outro número: "))

def calcular(n1,n2):
    soma = n1 + n2
    produto = n1 * n2
    return soma, produto
resultado_p , resultado = calcular(n1+n2)

print(f"soma: {resultado}")
print(f"produto: {resultado_p}")