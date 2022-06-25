class MatrizEsparsaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Passageiro:
    def __init__(self, nome:str, rg:str):
        self.__nome = nome
        self.__rg = rg
    
    @property
    def nome(self)->str:
        return self.__nome

    def __str__(self):
        return f'{self.__nome} RG {self.__rg}'


class MatrizEsparsa:
    def __init__(self, id:str, linhas:int, colunas:int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           ....
        '''
        self.__id = id
        self.__matriz = [ [ None for y in range( colunas ) ] 
             for x in range( linhas ) ]
        self.__passageiros = int()
        self.__linhas = len(self.__matriz)
        self.__colunas = len(self.__matriz[0])

    def tamanho(self)->int:
        '''Retorna a quantidade de células da matriz'''
        return self.__linhas * self.__colunas

    def estaVazia(self)->bool:
        return self.__passageiros == 0

    def estaCheio(self)->bool:
        return self.__passageiros == self.tamanho()

    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        if self.estaCheio():
            raise MatrizEsparsaException('Não há assento disponível.')
        
        else:
            for l in self.__linhas:
                for c in range(self.__colunas):
                    return self.numero_poltrona(l, c, self.__linhas)

    def pesquisar(self, numero_poltrona:int)->Passageiro:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        (l, c) = self.index_poltrona(numero_poltrona, self.__linhas)

        return self.__matriz[l][c]

    def pesquisaPassageiro(self, nome:str )->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        if self.estaVazia():
            raise MatrizEsparsaException('Este ônibus está vazio.')

        else:
            for l in range(self.__linhas):
                for c in range(self.__colunas):
                    if self.__matriz[l][c]:
                        if self.__matriz[l][c].nome.lower() == nome.lower():
                            return self.numero_poltrona(l, c, self.__linhas)

            return False

    def trocarPoltrona(self, poltrona_atual:int, nova_poltrona:int)->bool:
        (l, c) = self.index_poltrona(poltrona_atual, self.__linhas)
        (nl, nc) = self.index_poltrona(nova_poltrona, self.__linhas)
        
        if self.__matriz[nl][nc] is None:
            temp = self.__matriz[l][c]
            self.__matriz[l][c] = None
            self.__matriz[nl][nc] = temp

            return True

        raise MatrizEsparsaException("Este local já está ocupado.")

    def adicionar(self, passageiro: Passageiro, numero_poltrona:int)->bool:
        '''Retorna True se a inserção foi feita com sucesso, ou 
           False caso contrário'''
        if self.pesquisar(numero_poltrona) is None:
            (l, c) = self.index_poltrona(numero_poltrona, self.__linhas)

            self.__matriz[l][c] = passageiro
            self.__passageiros += 1

    def remover(self, numero_poltrona:int)->Passageiro:
        (l, c) = self.index_poltrona(numero_poltrona, self.__linhas)
        self.__matriz[l][c] = None

    def esvaziar(self):
        '''Esvazia a matriz esparsa'''
        self.__matriz = [ [ None for y in range( self.__colunas ) ] 
             for x in range( self.__linhas ) ]

    def mostrarAssentos(self):
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
                if self.__matriz[l][c] is None:
                    s += '[   ] '

                else:
                    s += f'[{self.__matriz[l][c].nome[:3].capitalize()}] '

            s+= '\n'

        temp = self.__linhas

        for j in range(self.__colunas):
            s += f'   {temp:^3}'
            temp += self.__linhas

        s += f'\n{self.__id}, {self.tamanho()} assentos.'

        return s
    
    @classmethod
    def numero_poltrona(cls, linha:int, coluna:int, linhas:int)->int:
        return (coluna * linhas + linha) + 1
    
    @classmethod
    def index_poltrona(cls, poltrona:int, linhas:int)->int:
        l = (poltrona-1) % linhas
        c = (poltrona-1) // linhas

        return l, c

if __name__ == '__main__':
    me = MatrizEsparsa('JPA-CG',4,3)
    print(me)
    me.adicionar(Passageiro("samuel", "123"), 6)
    me.adicionar(Passageiro("madu", "456"), 7)
    me.adicionar(Passageiro("gabriel", "789"), 8)
    print()
    print(me)
    print(me.pesquisaPassageiro("alex"))
    me.trocarPoltrona(6, 10)  
    me.remover(8)
    me.esvaziar()
    try: 
        me.mostrarAssentos()
    except MatrizEsparsaException as mee:
        print(mee)
