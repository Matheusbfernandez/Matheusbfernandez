print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


lado = input("Você esta em uma encruzilhada para onde deseja ir? Direita ou Esquerda?\n").lower()

if lado == "esquerda":
    print("parabens voce conseguiu chegar em um rio!")
elif lado == "direita":
    print("voce morreu! =( ")
    exit()
else:
    print("Voce digitou algo errado, comece denovo!")
    exit()

rio = input("Agora voce esta na beira de um rio! Voce deseja esperar um barco ou nadar ate o outro lado? Digite Esperar ou Nadar!\n").lower()
if rio == "esperar":
    print("Um barco acabou de chegar e voce conseguiu chegar a salvo para o outro lado!")
elif rio == "nadar":
    print("Voce acabou ficando sem forças e morreu nadando =(")
    exit()
else:
    print("Voce digitou algo errado, comece denovo!")
    exit()

porta = input("Depois de chegar ao outro lado voce se depara com 3 portas: qual voce escolhera? Vermelha, Azul ou Amarela\n").lower()
if porta == "amarela":
    print("Parabens voce encontrou o tesouro escondido!")
elif porta == "vermelha":
    print("Voce escolheu a porta errada e caiu em um buraco! Voce morreu")
    exit()
elif porta == "azul":
    print("Voce ficou preso numa armadilha e nao conseguirá sair! Fim de jogo")
    exit()
else:
    print("Voce digitou algo errado, comece denovo!")