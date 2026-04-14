def soma(a, b):
    try:
        return a + b
    
    except TypeError:
        print("entrada inválida")
        return 0

print(soma(5, 3))       
print(soma(5, "texto")) 
  