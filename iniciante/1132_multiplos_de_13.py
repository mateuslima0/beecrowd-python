contador = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    if valor % 13 == 0:
        contador += 1

print(f"{contador} Multiplo(s) de 13")
