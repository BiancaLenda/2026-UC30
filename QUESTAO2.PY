N = int(input()) 
R = int(input()) 
P = int(input()) 

total = N
dias = 0

while total < P:
    novos = N * (R ** dias)
    total += novos
    dias += 1
print(dias)
