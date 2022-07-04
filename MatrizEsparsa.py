class MatrizEsparsaException(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class MatrizEsparsa:
    # construtor
    def __init__(self, linhas:int, colunas:int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           ....
        '''
        self.__matriz = [ [ None for y in range( colunas ) ] 
             for x in range( linhas ) ]
        self.__unidades = int()
        self.__linhas = len(self.__matriz)
        self.__colunas = len(self.__matriz[0])
    
    @property
    def linhas(self)->int:
        return self.__linhas

    @property
    def colunas(self)->int:
        return self.__colunas
    
    @property
    def matriz(self)->object:
        return self.__matriz

    @property
    def unidades(self)->int:
        return self.__unidades

    def tamanho(self)->int:
        '''Retorna a quantidade de células da matriz'''
        return self.__linhas * self.__colunas

    # retorna True ou False caso a matriz esteja vazia
    def estaVazia(self)->bool:
        return self.__unidades == 0

    # retorna True ou False caso a matriz esteja cheia
    def estaCheia(self)->bool:
        return self.__unidades == self.tamanho()

    def pesquisar(self, posicao:int)->object:
        '''Retorna os dados de uma célula em
           uma determinada posição'''
        (l, c) = self.indices(posicao, self.__linhas)

        return self.__matriz[l][c]

    def pesquisarPosicao(self, chave:str )->int:
        '''Retorna o número da célula em que uma
           determinada chave está'''
        if self.estaVazia():
            raise MatrizEsparsaException('Esta Matriz está vazia.')
   
        for l in range(self.__linhas):
            for c in range(self.__colunas):
                if self.__matriz[l][c]:
                    if self.__matriz[l][c] == chave:
                        return self.indiceLinear(l, c, self.__linhas)

        return False

    # troca o objeto de uma célula para outra caso esteja vazia
    def trocar(self, posicao_atual:int, posicao_nova:int)->bool:
        (l, c) = self.indices(posicao_atual, self.__linhas)
        (nl, nc) = self.indices(posicao_nova, self.__linhas)
        
        if self.__matriz[l][c] is None:
            raise MatrizEsparsaException(f"A posição {posicao_atual} está vazia.")

        elif self.__matriz[nl][nc] is not None:
            raise MatrizEsparsaException(f"A posição {posicao_nova} já está preenchida.")
        
        temp = self.__matriz[l][c]
        self.__matriz[l][c] = None
        self.__matriz[nl][nc] = temp

        return True

    def adicionar(self, dado:object, posicao:int)->bool:
        '''Retorna True se a inserção foi feita com sucesso, ou 
           False caso contrário'''
        if self.pesquisar(posicao) is not None:
            raise MatrizEsparsaException(f"A posicao {posicao} já está preenchida.")

        (l, c) = self.indices(posicao, self.__linhas)
        self.__matriz[l][c] = dado
        self.__unidades += 1

        return True

    # remove o objeto de uma célula
    def remover(self, posicao:int)->object:
        (l, c) = self.indices(posicao, self.__linhas)
        temp = self.__matriz[l][c]

        if temp is None:
            raise MatrizEsparsaException(f"A posição {posicao} já está vazia.")

        self.__matriz[l][c] = None
        self.__unidades -= 1

        return temp
    
    # esvazia a matriz
    def esvaziar(self)->bool:
        '''Esvazia a matriz esparsa'''
        self.__matriz = [ [ None for y in range( self.__colunas ) ] 
             for x in range( self.__linhas ) ]

        self.__unidades = 0
        return True

    # exibe a matriz completa
    def exibirMatriz(self):
        '''Mostra o status de ocupacao de todos os assentos'''
        print(self.__str__())

    def __str__(self):
        s = ''

        for l in range(self.__linhas):
            for c in range(self.__colunas):
                if self.__matriz[l][c] is None:
                    s += '[   ] '

                else:
                    s += f'[{str(self.__matriz[l][c])[:3]:^3}] '

            s+= '\n'
            
        return s
    
    """
    PARTE CHAVE DO PROJETO:
    dois métodos de classe que calculam o indice linear
    e os indices normais de uma célula da matriz, dado a
    linha e a coluna da mesma ou o indice linear, respectivamente
    """
    @classmethod
    def indiceLinear(cls, linha:int, coluna:int, linhas:int)->int:
        return (coluna * linhas + linha) + 1
    
    @classmethod
    def indices(cls, poltrona:int, linhas:int)->int:
        l = (poltrona-1) % linhas
        c = (poltrona-1) // linhas

        return l, c
