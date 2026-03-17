#Exercício 1: Maior ou menor de idade: Peça a idade do usuário e mostre se é maior ou menor de idade
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else: 
    print("Você é menor de idade.")



#Exercício 2: Número positivo ou negativo: Peça um número ao usuário e mostre se é positivo ou negativo
num = int(input("Digite um número: "))

if num > 0:
    print("Número positivo")
elif num == 0:
    print("O número digitado é 0")
else:
    print("Número negativo")


#Exercício 3: Sistema de notas: Peça a nota do aluno. >= 7 Aprovado; >= 5 Recuperação; < 5 Reprovado
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado!!")
elif nota >= 5:
    print("Recuperação!!")
else:
    print("Reprovado!!")


#Exercício 4: Número par ou ímpar: Peça um número e diga se é par ou ímpar
num1 = int(input("Digite um número: "))
if num1 % 2 == 0:
    print("O número é par!!")
else:
    print("O número é ímpar!!")
