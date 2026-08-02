import sys

for linha in sys.stdin:
    linha = linha.strip()
    if linha == "":
        continue
    n = int(linha)
    print(n * n)
