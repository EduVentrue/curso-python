#Exercício 1: Peça ao usuário o nome, a idade, a altura e mostre "Seu nome é ______, você tem ______ anos e mede _____ metros."
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print(f"Seu nome é {nome}, você tem {idade} anos e mede {altura} metros.")

#Exercício 2: Peça dois números inteiros e mostre a soma, a subtração e a multiplicação
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"A soma é: {num1 + num2}") 
print(f"A subtração é: {num1 - num2}")
print(f"A multiplicação é: {num1 * num2}") 

#Exercício 3: Peça o peso e a altura do usuário e calcule o IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
print(f"O seu IMC é: {imc}")
