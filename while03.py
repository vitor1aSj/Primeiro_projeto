while True:
    opcao = int(input("""
    Menu
    1- somar
    2- Subtrair
    3- Multiplicar
    4- Dividir
    5- Sair"""))

    if opcao == 1:
        print("SOMAR")
    elif opcao == 2:
        print("Subtrair")
    elif opcao == 3:
        print("Multiplicar")
    elif opcao == 4:
        print("Dividir")
    elif opcao == 5:
        print("Saindo..")
        break
    else:
        print("Opção inválida, digite uma nova!")


