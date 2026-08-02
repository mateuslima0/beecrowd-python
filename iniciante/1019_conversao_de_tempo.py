segundos_totais = int(input())

horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(f"{horas}:{minutos}:{segundos}")
