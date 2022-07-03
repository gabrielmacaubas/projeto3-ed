from Onibus import *


onibus = {"JPA-CG": Onibus("JPA-CG", 4, 12), "JPaA-CG": Onibus("JPA-CG", 2, 4)}
print("""Bem-vindo ao Terminal MSG!
    
OPÇÕES:

    1 -> Comprar passagem 
    2 -> Trocar poltrona 
    3 -> Reembolso de passagem 
    4 -> Listar as linhas existentes
    5 -> Exibir linha
    6 -> Verificar poltrona
    7 -> Verificar passageiro
    0 -> encerra o programa""")

while True:
    comando = int(input('\n>>> '))
    
    if comando == 0:
        break
    
    elif comando == 1:
        print("\nDigite a linha desejada")

        linha = str(input("(Caso a linha não exista, uma será criada): "))
        nome = str(input("Digite seu nome: "))
        rg = int(input("Digite seu rg: "))

        passageiro = Passageiro(nome, rg)

        print("Poltrona desejada")

        poltrona = input("(Caso não escolhida, uma será selecionada): ")

        if poltrona == "":
            poltrona = None
        
        else:
            poltrona = int(poltrona)

        print()
        onibus[linha].alocar(passageiro, poltrona)
        onibus[linha].exibirOnibus()

    elif comando == 2:
        linha = str(input("\nDigite a linha desejada: ")) #fazer tratamento de exceção para caso usuário digitar linha inexistente
        poltrona_atual = int(input("Digite a poltrona a ser trocada: "))
        poltrona_nova = int(input("Digite a nova poltrona: "))
        
        onibus[linha].trocarPoltrona(poltrona_atual, poltrona_nova)
        onibus[linha].exibirOnibus()

    elif comando == 3:
        linha = str(input("\nDigite a linha desejada: "))
        poltrona_a_excluir = int(input('Digite o assento a ser reembolsado: '))
        passageiro = onibus[linha].retornarPassageiro(poltrona_a_excluir)

        continuar = str(input(f"{passageiro}\nDeseja excluir? (S/N): ")).upper()
        if continuar == "S":
            onibus[linha].desalocarPoltrona(poltrona_a_excluir)

        onibus[linha].exibirOnibus()
        
    elif comando == 4:
        print()

        for bus in list(onibus.keys()):
            print(bus)
    
    elif comando == 5:
        linha = str(input("\nDigite a linha desejada: "))

        onibus[linha].exibirOnibus()
    
    elif comando == 6:
        linha = str(input("\nDigite a linha desejada: "))
        passageiro = str(input('Digite o nome do passageiro: '))
        
        poltrona = onibus[linha].retornarPoltrona(passageiro)
        if poltrona:
            print(f"Poltrona: {onibus[linha].retornarPoltrona(passageiro)}")
        
        else:
            print(f"Passageiro não encontrado")
    elif comando == 7:
        linha = str(input('\nDigite a linha desejada: '))
        poltrona = int(input('Digite o número da poltrona: '))

        print(onibus[linha].retornarPassageiro(poltrona))
    
    else:
        print("Comando inválido.")
