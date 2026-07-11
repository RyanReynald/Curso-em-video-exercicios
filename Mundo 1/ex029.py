# Radar Eletrônico

Velocidade = int(input("Qual é a velocidade do carro? "))

multa = (Velocidade - 80) * 7

if Velocidade <= 80:
    print("Tenha um bom dia! dirija com segurança!")

else:
    print(f"""MULTADO! Você execedeu o limite permitido que é de 80km/h 
           Você deve pagar  Uma multa de R${multa}
             Tenha um bom dia! dirija com segurança! """)