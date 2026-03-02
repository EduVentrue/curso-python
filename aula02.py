print("Olá, seja bem-vindo a aula 2 do curso de Python")
print("Na aula de hoje, vamos aprender a usar os tipos de dados e a conversão de tipos")
print("Vamos começar!!")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Seu nome é {nome}, você tem {idade} anos e mede {altura} metros.")

print("Agora vamos realizar algumas contas com os números que você fornecer.")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2

print(f"A soma é: {soma}")
print(f"A subtração é: {sub}")
print(f"A multiplicação é: {mult}")

print("Agora vamos calcular seu IMC!!")

peso = float(input("Digite seu peso: "))
imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")