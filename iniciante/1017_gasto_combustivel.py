# URI/Beecrowd 1017 - Fuel Spent
# https://www.beecrowd.com.br/judge/pt/problems/view/1017
# Considera consumo fixo de 12 km por litro

distancia = float(input())
preco_litro = float(input())

gasto = (distancia / 12) * preco_litro
print(f"{gasto:.3f}")
