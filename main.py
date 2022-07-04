from Onibus import *
from pathlib import Path


# configurando main
largura = 4
comprimento = 12
path = str(Path(__file__).parent.resolve())+'/'
onibus = {"JPA-CG": Onibus("JPA-CG", largura, comprimento), "JPA-SP": Onibus("JPA-CG", largura, comprimento)}
onibus["JPA-SP"].alocar(Passageiro("Alex Sandro", 123))
onibus["JPA-SP"].alocar(Passageiro("Madu", 456), 8)
onibus["JPA-SP"].alocar(Passageiro("Macaúbas", 789), 16)
onibus["JPA-SP"].alocar(Passageiro("Sam", 101112), 30)

print("""Bem-vindo ao Terminal MSG!
    
OPÇÕES:

    1 -> Comprar passagem 
    2 -> Trocar poltrona 
    3 -> Reembolso de passagem 
    4 -> Listar as linhas existentes
    5 -> Exibir linha
    6 -> Verificar poltrona
    7 -> Verificar passageiro
    8 -> Gerar relação de uma viagem
    0 -> encerra o programa""")

while True:
    comando = int(input('\n>>> '))
    
    # comando para encerrar
    if comando == 0:
        break
    
    # comando para alocar passageiro
    elif comando == 1:
        print("\nDigite a linha desejada")

        linha = str(input("(Caso a linha não exista, uma será criada): "))

        # cria nova linha caso não haja uma com o mesmo nome
        if linha not in onibus:
            onibus[linha] = Onibus(linha, largura, comprimento)

            print("\nNOVA LINHA CRIADA\n")

        # recebe os dados do passageiro
        nome = str(input("Digite seu nome: "))
        rg = int(input("Digite seu rg: "))
        passageiro = Passageiro(nome, rg)

        print("Poltrona desejada")

        poltrona = input("(Caso não escolhida, uma será selecionada): ")

        # converte poltrona caso não seja informada
        if poltrona == "":
            poltrona = None
        
        else:
            poltrona = int(poltrona)

        print()

        # adiciona passageiro
        try:
            onibus[linha].alocar(passageiro, poltrona)
            onibus[linha].exibirOnibus()
        except OnibusException as oe:
            print(oe)

    # comando para trocar poltrona
    elif comando == 2:
        while True:
            linha = str(input("\nDigite a linha desejada: "))

            if linha in onibus:
                break

            print("Digite uma linha válida.")
            
        poltrona_atual = int(input("Digite a poltrona a ser trocada: "))
        poltrona_nova = int(input("Digite a nova poltrona: "))
        
        # troca poltrona
        try:
            onibus[linha].trocarPoltrona(poltrona_atual, poltrona_nova)
            onibus[linha].exibirOnibus()
        except OnibusException as oe:
            print(oe)

    # comando para desalocar passageiro
    elif comando == 3:
        while True:
            linha = str(input("\nDigite a linha desejada: "))
            
            if linha in onibus:
                break

            print("Digite uma linha válida.")

        poltrona_a_excluir = int(input('Digite o assento a ser reembolsado: '))

        # desaloca passageiro
        try:
            passageiro = onibus[linha].retornarPassageiro(poltrona_a_excluir)

            continuar = str(input(f"{passageiro}\nDeseja excluir? (S/N): ")).upper()
            if continuar == "S":
                onibus[linha].desalocarPoltrona(poltrona_a_excluir)
            
            print()

            onibus[linha].exibirOnibus()
        except OnibusException as oe:
            print(oe)
    
    # comando para exibir linhas
    elif comando == 4:
        print("\n--Linhas--")

        for bus in list(onibus.keys()):
            print(bus)
    
    # comando para exibir linha
    elif comando == 5:
        while True:
            linha = str(input("\nDigite a linha desejada: "))
            
            if linha in onibus:
                break

            print("Digite uma linha válida.")

        onibus[linha].exibirOnibus()
    
    # comando para encontrar poltrona de um passageiro
    elif comando == 6:
        while True:
            linha = str(input("\nDigite a linha desejada: "))
            
            if linha in onibus:
                break

            print("Digite uma linha válida.")

        passageiro = str(input('Digite o nome do passageiro: '))
        
        # procura poltrona
        try:
            poltrona = onibus[linha].retornarPoltrona(passageiro)

            if poltrona:
                print(f"Poltrona: {poltrona}")
            
            else:
                print(f"Passageiro não encontrado")
        except OnibusException as oe:
            print(oe)

    # comando para encontrar um passageiro em uma poltrona
    elif comando == 7:
        while True:
            linha = str(input("\nDigite a linha desejada: "))
            
            if linha in onibus:
                break

            print("Digite uma linha válida.")

        poltrona = int(input('Digite o número da poltrona: '))

        # procura passageiro
        try:
            print(onibus[linha].retornarPassageiro(poltrona))
        except OnibusException as oe:
            print(oe)
    
    # comando para gerar relação de passageiros de uma linha
    elif comando == 8:
        while True:
            linha = str(input("\nDigite a linha desejada: "))
            
            if linha in onibus:
                break

            print("Digite uma linha válida.")

        # recebe index do onibus no dicionario de linhas
        numero_linha = (list(onibus.keys()).index(linha))+1

        try:      
            # abre arquivo de texto  
            with open(path+'db.txt', 'w', encoding='utf-8') as f: 
                string = ""
                
                # preenche string com onibus vazio caso esteja
                if onibus[linha].estaVazio():
                    string += f"Linha {linha}-{numero_linha:0>3} - Ônibus vazio"

                # caso não esteja, preenche string com relação
                else:   
                    string += f"Linha: {linha}-{numero_linha:0>3}\nPoltrona;passageiro;rg\n"

                    for j in range(comprimento):
                        for i in range(largura):
                            if onibus[linha].localizar(i, j) is not None:
                                passageiro = onibus[linha].localizar(i, j)
                                poltrona = onibus[linha].numeroPoltrona(i, j)
                                string += f"{poltrona};{passageiro.nome};{passageiro.rg}\n"

                # preenche arquivo de texto com a string
                f.write(string)
        except OnibusException as oe:
            print(oe)

        print("\nRelação gerada com sucesso!\n\n", string)

    else:
        print("Comando inválido.")

print("--\nPrograma encerrado--")
