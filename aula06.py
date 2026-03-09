#Nesta aula vamos aprender um pouco sobre lista

#Atividade 1: Crie uma lista com 5 números inteiros e mostre todos eles usando print
numeros = [1, 2, 3, 4, 5]
print(numeros)

#Atividade 2: Crie uma lista com 3 cores. Mostre a primeira cor e a última cor.
print("---------------------------")
cores = ["amarelo", "azul", "rosa"]
print(cores[0])
print(cores[2])

#Atividade 3: Crie uma lista com os números [5, 10, 15]. Depois altere o número 10 para 20 e mostre a lista final
print("----------------------------")
numero1 = [5, 10, 15]
print(numero1)
numero1[1] = 20
print(numero1)

#Atividade 4: Crie uma lista com 3 frutas. Depois adicione mais uma fruta usando append(), mostre a lista
print("-----------------------------")
frutas = ["pera", "abacaxi", "melancia"]
print(frutas)
frutas.append("maçã")
print(frutas)

#Atividade 5: Crie uma lista com 4 nomes e utilize a função for para mostrar os itens
print("------------------------------")
nomes = ["Nathaly", "Adriana", "Eduardo", "Betina"]
for nome in nomes:
    print(nome)

#Atividade 6: Faça um programa que crie uma lista vazia. Peça ao usuário 3 números. Armazene esses números na lista. Mostre a lista final
print("---------------------------")
numero = []
for i in range(3):
    num = int(input(f"Digite o {i+1}º número: "))
    numero.append(num)

print(f"A lista final é: {numero}")
