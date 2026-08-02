# URI/Beecrowd 1009 - Salary with Bonus
# https://www.beecrowd.com.br/judge/pt/problems/view/1009

salario_fixo = float(input())
vendas = float(input())

total = salario_fixo + vendas * 0.15
print(f"TOTAL = {total:.2f}")
