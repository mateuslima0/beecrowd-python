# URI/Beecrowd 1099 - Sum of Consecutive Odd Numbers II
# https://www.beecrowd.com.br/judge/pt/problems/view/1099
# A soma dos N primeiros numeros impares e igual a N ao quadrado.
# O problema tem varios casos de teste ate o fim da entrada (EOF).

import sys

for linha in sys.stdin:
    linha = linha.strip()
    if linha == "":
        continue
    n = int(linha)
    print(n * n)
