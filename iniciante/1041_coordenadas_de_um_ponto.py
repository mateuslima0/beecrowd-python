# URI/Beecrowd 1041 - Coordinates of a Point
# https://www.beecrowd.com.br/judge/pt/problems/view/1041

x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")
