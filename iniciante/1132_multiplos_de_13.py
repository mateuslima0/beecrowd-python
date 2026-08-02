# URI/Beecrowd 1132 - Multiples of 13
# https://www.beecrowd.com.br/judge/pt/problems/view/1132
# Le valores ate encontrar o 0, que encerra a entrada e nao entra na contagem

contador = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    if valor % 13 == 0:
        contador += 1

print(f"{contador} Multiplo(s) de 13")
