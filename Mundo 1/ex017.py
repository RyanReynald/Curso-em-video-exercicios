#Catetos e Hipotenusa


#Importando biblioteca
import math

oposto = float(input(f"Comprimento do cateto oposto: "))
adj = float(input(f"Comprimento do cateto adjcente: "))

hi = math.hypot(oposto, adj)

print(f"A hipotenusa vai medir {hi:.2f} ")



#Sem importa biblioteca
oposto = float(input(f"Comprimento do cateto oposto: "))
adj = float(input(f"Comprimento do cateto adjcente: "))

hi = (oposto ** 2 + adj ** 2) **  (1/2)

print(f"A hipotenusa vai medir {hi:.2f} ")

