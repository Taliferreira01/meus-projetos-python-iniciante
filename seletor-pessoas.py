"""Seletor de Pessoas
Este programa solicita informações sobre sexo, idade e cor do cabelo de várias pessoas, é um dos desafios do curso de Python Iniciante no curso em vídeo, apresentado
pelo professor Gustavo Guanabara.
Ele conta quantos homens com mais de 18 anos têm cabelo castanho e quantas mulheres com mais de 30 anos têm cabelo loiro.
"""

soma_idade_cabelo = 0
soma_idade_loiro = 0
resposta = ""
while True:
    print("=========================================")
    print("|         Seletor de pessoas !          |")
    print("=========================================")
    sexo = str(input("Qual sexo [F/M] ? ")).upper()
    if sexo != "F" and sexo != "M":
        print("Sexo inválido, tente novamente.")
        continue

    idade = int(input("Qual a idade ? "))
   
    cabelo = int(input("Qual a cor do cabelo? \n [1] para Preto, \n [2] para castanho, \n [3] para loiro, \n [4] para ruivo. \n qual sua escolha ? "))
    if cabelo != 1 and cabelo != 2 and cabelo != 3 and cabelo != 4:
        print("Cor de cabelo inválida, tente novamente.")
        continue

    if sexo == "M" and idade > 18 and cabelo == 2:
        soma_idade_cabelo += 1
    elif sexo == "F" and idade > 30 and cabelo == 3:
        soma_idade_loiro += 1
        
    resposta = str(input("Você deseja continuar ? [S/N] ")).upper()

    if resposta != "S":
        print("=========================================")
        print(f"Total de homens com mais de 18 anos e cabelo castanho: {soma_idade_cabelo}")
        print(f"Total de mulheres com mais de 30 anos e cabelo loiro: {soma_idade_loiro}")
        print("=========================================")
        break
        

