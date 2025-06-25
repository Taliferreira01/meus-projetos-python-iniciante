# Este programa foi desenvolvido como parte de um desafio proposto nas aulas de introdução à programação.
# O objetivo da atividade é implementar um programa utilizando laços de repetição (estrutura while)
# para realizar contagens progressiva (de 0 a 10) e regressiva (de 10 a 0)

while True:
    print("*---------------------------------------*")
    print("| Faça sua escolha !                    |")
    print("| Pressione 1 para contar (0 a 10)      |")
    print("| Pressione 2 para contar de (10 a 0)   |")
    print("| Pressione 3 para sair                 |")
    print("*---------------------------------------*")
#interação para o usuário
    resposta = int(input("Qual sua escolha? "))
#inicio, com contagem progressiva
    if resposta == 1:
        cont = 0
        while cont <= 10:
            print(cont)
            cont += 1
        break    
#contagem regressiva
    elif resposta == 2:
        cont = 10
        while cont >= 0:
            print(cont)
            cont -= 1
        break
# encerra o programa       
    elif resposta == 3:
        print("Programa encerrado!")
        break  
# Se o usuário digitar a opção invalida, volta para o laço        
    else:
        print("Você escolheu uma opção inválida, tente novamente!")
