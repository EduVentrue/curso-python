#Aula 5: Nesta aula vamos aprender a utilizar Estruturas de Repetição

#Atividade 1: Use while para imprimir número de 0 a 10
print("Primeiro vamos imprimir os números de 0 até 10.")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1

#Atividade 2: Use for para imprimir número pares de 0 a 20
print("------------------------")
print("Agora vamos imprimir os números pares de 0 até 20")
i = 0
for i in range(0, 21, 2):
    print(i)

#Atividade 3: crie um programa que peça uma senha, enquanto a senha for diferente de "1234", peça novamente, quando acertar
#mostre "Acesso Liberado!".
print("------------------------")
print("Vamos simular um programa de reconhecimento de senhas")
senha = input("Digite a senha: ")
while senha != "1234":
    print("Senha incorreta!! Tente novamente.")
    senha = input("Digite a senha: " )
    if senha == "1234":
        print("Acesso Liberado")
        break

#Atividade 4: peça um número e mostre a tabuada dele de 1 a 10
print("------------------------")
print("Para finalizar, vamos fazer uma tabuada.")
numero = int(input("Digite um número para mostrarmos a tabuada dele: "))
contador2 = 1

while contador2 != 11:
    resultado = numero * contador2
    print(f"{numero} x {contador2} = {resultado}")
    contador2 += 1
    if contador2 == 11:
        break
