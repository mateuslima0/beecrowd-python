# URI/Beecrowd 1038 - Snack
# https://www.beecrowd.com.br/judge/pt/problems/view/1038

codigo = int(input())
quantidade = int(input())

precos = {
    1: 4.00,  # X-Burguer
    2: 4.50,  # X-Egg
    3: 5.00,  # X-Bacon
    4: 2.00,  # Hamburguer
    5: 2.50,  # Cheeseburguer
    6: 1.50,  # Cachorro Quente
}

total = precos[codigo] * quantidade
print(f"Total: R$ {total:.2f}")
