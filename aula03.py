#Esse programa tem por objetivo a utilização e o entendimento de Operadores Lógicos
#Base fundamental para a função if que veremos na próxima aula

#Nesse primeiro momento vamos resolver expressões aritméticas com algum número digitado pelo usuário
print("Vamos fazer algumas operações matemáticas?")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo núemro: "))
soma = num1 + num2
divis = num1 // num2
resto_divis = num1 % num2

print(f"A soma dos número é: {soma}")
print(f"A divisão inteira dos números é: {divis}")
print(f"O resto da divisão é: {resto_divis}")

#Agora vamos criar um pequeno programa para saber se o usuário é maior ou menor de idade
print("Vamos verificar se o usuário é maior de idade?")
idade = int(input("Digite sua idade: "))
maior_idade = idade > 18
print("O usuário é maior de idade?", maior_idade)

#Agora, para finalizar a aula, vamos calcular a média de algumas notas digitadas pelo usuário
print("Vamos calcular a média de algumas notas?")
nota1 = float(input("Digite a primeira nota para o cálculo da média: "))
nota2 = float(input("Digite a segunda nota para o cálculo da média: "))
media = (nota1 + nota2)/2
nota_final = media > 7
print("A nota final é maior de que 7?", nota_final)