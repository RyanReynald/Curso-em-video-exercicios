#Seno, Cosseno e Tangente

from math import radians, sin, cos, tan

angulo = int(input('Digite o ângulo de que você deseja: '))

seno = sin(radians(angulo))
print(f"O ângulo de {angulo} tem seno de {seno:.2f}")

cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem seno de {cosseno:.2f}")

tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem seno de {tangente:.2f}")