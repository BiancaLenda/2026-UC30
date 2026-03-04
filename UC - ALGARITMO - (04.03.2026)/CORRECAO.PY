n1=float(input("Digite um numero:"))
n2=float(input("Digite um numero:"))

soma=n1+n2
mult=n1*n2
print(f"a soma é {soma} o produto é {mult}")





n1=int(input("digite um numero:"))
if n1<0:
    print("numero invalido")
elif n1 %2 ==0:
    quadrado=n1*n1
    print(f"seu numero é par sendo o quadrado {quadrado}")
else:
    cubo=n1*n1*n1
    print(f"seu numero é impar sendo o cubo é {cubo}")




usuario=input("digite seu login:")
senha=input("Digite sua senha:")

if usuario ==" procopio" and senha=="12345":
    print("acesso liberado")

elif usuario=="paiva" and senha=="54321":
     print("acesso liberado")

else:
     print("acesso negado")




nome=input("digite seu nome:")
for tentativa in range(3, 0, -1):
   senha = int(input("Digite sua senha: ")) 

   if senha == 123456:
     print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
     break 
   
   else:
       if tentativa > 1:
         print(f"Senha incorreta! Você ainda tem {tentativa - 1} tentativa(s).")
       else: 
          print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
