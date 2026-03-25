def media_total(*numeros):
    n1 = float(input("Digite sua nota: "))
    n2 = float(input("Digite sua nota: "))

    total = 0 
    notas = [n1 + n2]
    for num in n1,n2:
        total += num
    return total 