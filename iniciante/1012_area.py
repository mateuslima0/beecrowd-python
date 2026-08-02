# URI/Beecrowd 1012 - Area
# https://www.beecrowd.com.br/judge/pt/problems/view/1012

a = float(input())
b = float(input())
c = float(input())
pi = 3.14159

triangulo = (a * b) / 2
circulo = pi * c * c
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
