rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

jogada = ["rock", "paper", "scissors"]

suajogada = input("Escolha pedra, papel e tesoura: 0 para pedra 1 para papel e 2 para tesoura\n")

if suajogada == "0":
    print(rock)
elif suajogada == "1":
    print(paper)
elif suajogada == "2":
    print(scissors)
else:
    print("sua jogada nao foi valida!")
    exit()


jogadapc = (random.choice(jogada))
if jogadapc == "rock":
    print(rock)
elif jogadapc == "paper":
    print(paper)
else:
    print(scissors)

if suajogada == "0" and jogadapc == "paper":
    print("Voce perdeu!")
elif suajogada == "0" and jogadapc == "scissors":
    print("Voce ganhou!")
elif suajogada == "1" and jogadapc == "rock":
    print("Voce ganhou!")
elif suajogada == "1" and jogadapc == "scissors":
    print("Voce perdeu!")
elif suajogada == "2" and jogadapc == "rock":
    print("Voce perdeu!")
elif suajogada == "2" and jogadapc == "paper":
    print("Voce ganhou!")
else:
    print("Empate!!")
