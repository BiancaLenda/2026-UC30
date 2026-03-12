print("python é fácil")
print("python é fácil")
print("python é fácil")

#com f(x)
def exibirmensagem():
    print("Olá mundo!")

exibirmensagem()

#f(x) com parametro
def saudar(nome):
    print(f"Olá, {nome}")

saudar("Ana")
saudar("Bruno")

def exibirmensagem(nome, mensagem):
    print(f"{mensagem},{nome}")

exibirmensagem("ana","bom dia")

exibirmensagem(nome = "Bruno", mensagem = "boa noite")

#f(x) que retorna média
def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularMedia(8.0, 9.0)
print(f"Média: {resultado}")

nome = input("digite seu nome:")
def exibirmensagem(nome):
    print(f"olá, {nome}")
