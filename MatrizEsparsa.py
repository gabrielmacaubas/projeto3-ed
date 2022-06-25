class MatrizEsparsaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

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
        self.__unidades = int()
        self.__linhas = len(self.__matriz)
        self.__colunas = len(self.__matriz[0])

    def tamanho(self)->int:
        '''Retorna a quantidade de células da matriz'''
        return self.__linhas * self.__colunas

    def estaVazia(self)->bool:
        return self.__unidades == 0

    def estaCheio(self)->bool:
        return self.__unidades == self.tamanho()

    def pesquisar(self, posicao:int)->object:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        (l, c) = self.indices(posicao, self.__linhas)

        return self.__matriz[l][c]

    def pesquisarPosicao(self, chave:str )->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        if self.estaVazia():
            raise MatrizEsparsaException('Esta Matriz está vazia.')
   
        for l in range(self.__linhas):
            for c in range(self.__colunas):
                if self.__matriz[l][c]:
                    if self.__matriz[l][c] == chave:
                        return self.indice_linear(l, c, self.__linhas)

        return False

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
    
    def remover(self, posicao:int)->object:
        (l, c) = self.indices(posicao, self.__linhas)
        temp = self.__matriz[l][c]

        if temp is None:
            raise MatrizEsparsaException(f"A posição {posicao} já está vazia.")

        self.__matriz[l][c] = None
        self.__unidades -= 1

        return temp

    def esvaziar(self):
        '''Esvazia a matriz esparsa'''
        self.__matriz = [ [ None for y in range( self.__colunas ) ] 
             for x in range( self.__linhas ) ]

        self.__unidades = 0

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
    
    @classmethod
    def indice_linear(cls, linha:int, coluna:int, linhas:int)->int:
        return (coluna * linhas + linha) + 1
    
    @classmethod
    def indices(cls, poltrona:int, linhas:int)->int:
        l = (poltrona-1) % linhas
        c = (poltrona-1) // linhas

        return l, c

if __name__ == '__main__':
    a = MatrizEsparsa("a", 4, 12)
    a.adicionar(1234, 4)
    a.adicionar(5678, 5)
    a.exibirMatriz()
