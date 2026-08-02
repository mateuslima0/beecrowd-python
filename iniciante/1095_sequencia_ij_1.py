# URI/Beecrowd 1095 - Sequence IJ 1
# https://www.beecrowd.com.br/judge/pt/problems/view/1095

n = int(input())
m = int(input())

for i in range(1, n + 1):
    for j in range(i, m + 1):
        print(f"I={i} J={j}")
