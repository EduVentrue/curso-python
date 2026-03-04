#Nesta aula, iremos aprender sobre estruturas condicionais

#Atividade 1: Fazer um programa que peça ao usuário uma nota e mostre se está aprovado
print("Olá, vamos verificar se o aluno está aprovado?")
nota = float(input("Digite a nota final do aluno: "))
if nota >= 7:
    print("Aprovado!!")
else:
    print("Não foi dessa vez. Reprovado!!")


#Atividade 2: Peça um número e diga se ele é positivo, negativo ou zero
print("Agora vamos verificar se um número é positivo ou negativo.")
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número digitado é positivo!!")
elif numero < 0:
    print("O número digitado é negativo!!")
else:
    print("O número digitado é 0")

#Atividade 3: Peça a idade e se possui carteira e mostre "Pode dirigir ou Não pode dirigir"
print("Agora vamos verificar se alguém tem licença para dirigir")
idade = int(input("Digite sua idade: "))
tem_carteira = input("Tem carteira (s/n): ").lower
resposta = tem_carteira == "s"

if idade >= 18 and resposta:
    print("Pode dirigir!!")
else:
    print("Não pode dirigir")