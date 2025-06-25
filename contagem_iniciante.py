while True:
    print('*---------------------------------------*')
    print("| Faça sua escolha !                    |")
    print("| Pressione 1 para contar (0 a 10)      |")
    print("| Pressione 2 para contar de (10 a 0)   |")
    print("| Pressione 3 para sair                 |")
    print('*---------------------------------------*')

    resposta = int(input("Qual sua escolha? "))

    if resposta == 1:
        cont = 0
        while cont <= 10:
            print(cont)
            cont += 1
        break    

    elif resposta == 2:
        cont = 10
        while cont >= 0:
            print(cont)
            cont -= 1
        break
    elif resposta == 3:
        print("Programa encerrado!")
        break  # Encerra o loop

    else:
        print("Você escolheu uma opção inválida, tente novamente!")