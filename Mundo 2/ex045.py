#GAME: Pedra Papel e Tesoura

from random import randint
from time import sleep

print(""" Sua opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA""")

lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Qual Sua Jogada? '))
computador = randint(0, 2)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")


print("-=-" * 20)
print(f"Computador jogou {lista[computador]}")
print(f"Jogador jogou {lista[jogador]}")
print("-=-" * 20)

if computador == 0:
    if jogador == 0:
        print("EMPATOU")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVÀLIDA!")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATOU")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÀLIDA!")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATOU")
    else:
        print("JOGADA INVÀLIDA!")
else:
    print("JOGADA INVÀLIDA!")