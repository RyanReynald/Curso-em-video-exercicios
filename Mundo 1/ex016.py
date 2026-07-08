#quebrando número


#importando biblioteca 

from math import trunc

n = float(input("Digite um valor: "))

print(f"O valor digitado foi {n} e sua porção inteira é {trunc(n)}")


#Sem importa biblioteca

n = float(input("Digite um valor: "))
print(f"O valor digitado foi {n} e sua porção inteira é {int(n)}")