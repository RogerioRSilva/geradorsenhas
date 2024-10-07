import datetime
import random

print(" =========== GERADOR DE SENHAS ============== ")

senha = []

for c in range(0, 6):
    senha.append(random.randrange(0, 9))

for a in range(0 ,6):
    for b in range(0, 6):
        if (senha[a] == senha[b]):
            senha.pop(a)
            senha.append(random.randrange(0, 9))



with open('senhaGerada.txt', 'w') as arquivo:
    arquivo.write('Senha Gerada: ' + str(senha).replace(',', ' '))

with open('senhaGerada.txt', 'a') as arquivo:
    arquivo.write('\nData / hora: ' + str(datetime.datetime.now()))



