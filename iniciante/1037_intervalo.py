# URI/Beecrowd 1037 - Interval
# https://www.beecrowd.com.br/judge/pt/problems/view/1037

x = float(input())

if x < 0 or x > 100:
    print("Fora de intervalo")
elif x < 25:
    print("Intervalo [0,25)")
elif x < 50:
    print("Intervalo [25,50)")
elif x < 75:
    print("Intervalo [50,75)")
else:
    print("Intervalo [75,100]")
