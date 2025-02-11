



print("Bem vindo a calculadora de contas!")

conta_total = float(input("Qual o valor total da conta?\n"))
gorjeta = int(input("Qual a porcentagem de gorjeta? 10, 12, 15\n"))
gorjetat = 1 + gorjeta/100
numero_pessoas = int(input("quantas pessoas vão dividir a conta?\n"))
valor = float((conta_total / numero_pessoas) * gorjetat)
valor_total = float(round(valor, 2))

print(f"O valor por pessoa é: {valor_total} ")






