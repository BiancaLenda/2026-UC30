def divisao(x, y):
    try:
        return x / y
    
    except ZeroDivisionError:
        return "não divida por zero!"

print(divisao(10, 2))   
print(divisao(10, 0)) 