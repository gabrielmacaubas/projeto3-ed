class Passageiro:
    def __init__(self, nome:str, rg:str):
        self.__nome = nome
        self.__rg = rg
    
    @property
    def nome(self)->str:
        return self.__nome

    def __str__(self):
        return f'{self.__nome} RG {self.__rg}'


class Onibus:
    def __init__(self):
    
    
    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        if self.estaCheio():
            raise MatrizEsparsaException('Não há assento disponível.')
        
        else:
            for l in self.__linhas:
                for c in range(self.__colunas):
                    return self.numero_poltrona(l, c, self.__linhas)
                
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

"""
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
"""