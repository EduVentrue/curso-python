#Exercícios 1: Contagem simples: Mostre números de 1 a 10 usando while e for

contador = 0
while contador <= 10:
    print(contador)
    contador += 1
print("-------------------------")

for cont in range(11):
    print(cont)

print("-------------------------")


#Exercícios 2: Soma de Números: Peça um número ao usuário. Mostre a soma de todos os números anteriores até chegar no número digitado
num = int(input("Digite um número: "))
soma = 0
expressao = ""

for i in range(1, num + 1):
    soma += i

    if i == num:
        expressao += str(i)
    else:
        expressao += str(i) + " + "
print(f"{expressao} = {soma}")
print("-------------------------------------")

#Exercício 3: Tabuada: Peça um número e mostre até a tabuada do 10
numero = int(input("Digite o número que deseja saber a tabuada: "))
for a in range (1, 11):
    operacao = numero * a
    print(f"{numero} x {a} = {operacao}")
print("--------------------------------------")

#Exercício 4: Contador Regressivo: Mostre de 10 até 1 com while e for
num1 = 10
while num1 >= 0:
    print(num1)
    num1 -= 1

#Exercício 5: Sistema de Repetição: Enquanto o usuário digitar "s", o programa continua
escolha = input("Vamos cadastras alguns alunos? s/n ")
alunos = []
while escolha == "s":
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    escolha = input("Quer cadastrar outro aluno? s/n ")
print(alunos)