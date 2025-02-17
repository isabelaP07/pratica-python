import random

print ('Bem Vindo no jogo de adivinhação') 

numero_secreto =random.randrange(1,101)  
total_de_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade")
print("(1) Fácil (2) Médio (3) Dificil")

nível = int(input("Ddefina o nível: "))

if(nível == 1):
    total_de_tentativas = 20
elif(nível == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1,total_de_tentativas +1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um número entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!" .format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos


print("Fim do jogo")
   