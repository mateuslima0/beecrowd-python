# URI/Beecrowd 1133 - Rest of a Division
# https://www.beecrowd.com.br/judge/pt/problems/view/1133
# Le pares de valores ate encontrar "0 0", que encerra a entrada

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a % b)
