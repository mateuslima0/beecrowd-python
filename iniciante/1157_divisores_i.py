# URI/Beecrowd 1157 - Divisors I
# https://www.beecrowd.com.br/judge/pt/problems/view/1157

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
