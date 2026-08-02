# URI/Beecrowd 1153 - Simple Factorial
# https://www.beecrowd.com.br/judge/pt/problems/view/1153

n = int(input())
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"{n}!={fatorial}")
