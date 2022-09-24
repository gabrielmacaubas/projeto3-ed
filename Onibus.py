from MatrizEsparsa import *
from Passageiro import Passageiro

class OnibusException(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class Onibus:
    # construtor
    def __init__(self, id:str, linhas:int, colunas:int):
        self.__onibus = MatrizEsparsa(linhas, colunas)
        self.__id = id
        self.__linhas = self.__onibus.linhas
        self.__colunas = self.__onibus.colunas
    
    # número de passageiros alocados no ônibus
    def passageiros(self)->int:
        return self.__onibus.unidades

    def tamanho(self)->int:
        '''Retorna a quantidade de assentos do ônibus'''
        return self.__onibus.tamanho()

    # retorna o objeto do assento dado a linha e a coluna
    def localizar(self, linha:int, coluna:int)->object:
        return self.__onibus.matriz[linha][coluna]
    
    # retorna True ou False caso o ônibus esteja vazio ou não
    def estaVazio(self)->bool:
        return self.__onibus.estaVazia()

    # retorna True ou False caso o ônibus esteja cheio ou não
    def estaCheio(self)->bool:
        return self.__onibus.estaCheia()
    
    # retorna o número de uma poltrona dado a linha e a coluna
    def numeroPoltrona(self, linha:int, coluna:int)->int:
        return self.__onibus.indiceLinear(linha, coluna, self.__linhas)

    # procura assento disponível através de varredura
    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        if self.estaCheio():
            raise OnibusException('Não há assento disponível.')
        
        else:
            for c in range(self.__colunas):
                for l in range(self.__linhas):      
                    if self.localizar(l, c) is None:
                        return self.numeroPoltrona(l, c)
    
    # aloca passsageiro no ônibus
    def alocar(self, passageiro:object, poltrona=None)->bool:
        '''Retorna True se a inserção foi feita com sucesso, ou 
           False caso contrário'''
        if poltrona is None:
            self.alocar(passageiro, self.procurarAssentoDisponivel())
        else:
            try:  
                return self.__onibus.adicionar(passageiro, poltrona)
            except MatrizEsparsaException as me:
                raise OnibusException("Este assento não existe")

    # troca poltrona
    def trocarPoltrona(self, poltrona:int, nova_poltrona:int)->bool:
        try:
            return self.__onibus.trocar(poltrona, nova_poltrona)
        except MatrizEsparsaException:
            raise OnibusException("Este assento já está ocupado.")
    
    # desaloca poltrona
    def desalocarPoltrona(self, poltrona:int)->bool:
        try:
            return self.__onibus.remover(poltrona)
        except MatrizEsparsaException:
            raise OnibusException("Este assento já está vazio.")

    # retorna número da poltrona dado o nome do passageiro
    def retornarPoltrona(self, nome_passageiro:str)->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        if self.estaVazio():
            raise OnibusException('Esta Matriz está vazia.')
   
        for l in range(self.__linhas):
            for c in range(self.__colunas):
                if self.localizar(l, c):
                    if self.localizar(l, c).nome == nome_passageiro:
                        return self.numeroPoltrona(l, c)

        return False

    # retorna objeto do passageiro dado o número da poltrona
    def retornarPassageiro(self, poltrona:int)->object:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        if self.__onibus.pesquisar(poltrona) is None:
            raise OnibusException('Este assento está vazio.')

        return self.__onibus.pesquisar(poltrona)

    # esvazia o ônibus
    def esvaziarOnibus(self)->bool:
        '''Esvazia o onibus'''
        return self.__onibus.esvaziar()
    
    # exibe o ônibus
    def exibirOnibus(self):
        '''Mostra o status de ocupacao de todos os assentos'''
        print(self.__str__())

    def __str__(self):
        s = ''
        i = 0
        temp = 1

        for j in range(self.__colunas):
            s += f'   {temp:^3}'
            temp += self.__linhas
            
        s += '\n'

        for l in range(self.__linhas):
            i += 1
            s += f'{i}-'

            for c in range(self.__colunas):
                if self.localizar(l, c) is None:
                    s += '[   ] '

                else:
                    s += f'[{self.localizar(l, c).nome[:3].capitalize():>3}] '

            s+= '\n'

        temp = self.__linhas

        for j in range(self.__colunas):
            s += f'   {temp:^3}'
            temp += self.__linhas

        s += f'\n{self.__id}, {self.tamanho()-self.__onibus.unidades} assentos disponiveis.'

        return s
