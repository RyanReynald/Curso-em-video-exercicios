#jogo da Adivinhação v.1.0

from random import randint
from time import sleep

print("-=--" * 20)
print("Vou pensar em um número entre 0 e 5 tente adivinhar")
print("-=--" * 20)

n = int(input("Em que número eu pensei? "))

print("Processando...")

sleep(2)

computador = randint(0, 5)

if n == computador:
    print("PARABENS! você conseguiu me vencer!")

else: 
    print(f"Ganhei eu pensei no número {computador} e não no {n}!")