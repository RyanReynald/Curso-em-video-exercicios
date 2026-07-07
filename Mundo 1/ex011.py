#Pintando Parede

larg = float(input("largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt

print(f"Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m")

tinta = area / 2

print(f"Para pintar essa parede, você precisará de {tinta}L de tinta")