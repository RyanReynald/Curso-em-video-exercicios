#Cores terminal

print("\033[0;31;43m Hello world!\033[m")

a = 5
b = 5

print(f"Os valores sao \033[32m{a}\033[m e \033[31m{b}\033[m!!")

#outro exemplo (utilizando dicionario)

nome = "Ryan"
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m',
    'vermelho':'\033[31m',
}

print(f"Olá! muito prazer em te conhecer, {cores['vermelho']}{nome}{cores['limpa']}")