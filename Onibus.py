from MatrizEsparsa import MatrizEsparsa
from Passageiro import Passageiro
from pathlib import Path

class OnibusException(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)


class Onibus:
    def __init__(self, id:str, linhas:int, colunas:int):
        self.__onibus = MatrizEsparsa(linhas, colunas)
        self.__id = id
        self.__linhas = self.__onibus.linhas
        self.__colunas = self.__onibus.colunas
    
    def tamanho(self)->int:
        return self.__onibus.tamanho()

    def localizar(self, linha:int, coluna:int)->object:
        return self.__onibus.matriz[linha][coluna]
    
    def estaVazio(self)->bool:
        return self.__onibus.estaVazia()

    def estaCheio(self)->bool:
        return self.__onibus.estaCheia()
    
    def numeroPoltrona(self, linha:int, coluna:int)->int:
        return self.__onibus.indiceLinear(linha, coluna, self.__linhas)

    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        if self.estaCheio():
            raise OnibusException('Não há assento disponível.')
        
        else:
            for l in range(self.__linhas):
                for c in range(self.__colunas):
                    return self.numeroPoltrona(l, c)
    
    def alocar(self, passageiro:object, poltrona=None)->bool:
        if poltrona is None:
            self.alocar(passageiro, self.procurarAssentoDisponivel())
        else:
            return self.__onibus.adicionar(passageiro, poltrona)

    def trocarPoltrona(self, poltrona:int, nova_poltrona:int)->bool:
        return self.__onibus.trocar(poltrona, nova_poltrona)
    
    def desalocarPoltrona(self, poltrona:int)->bool:
        return self.__onibus.remover(poltrona)

    def retornarPoltrona(self, nome_passageiro:str)->int:
        if self.estaVazio():
            raise OnibusException('Esta Matriz está vazia.')
   
        for l in range(self.__linhas):
            for c in range(self.__colunas):
                if self.localizar(l, c):
                    if self.localizar(l, c).nome == nome_passageiro:
                        return self.numeroPoltrona(l, c)

        return False

    def retornarPassageiro(self, poltrona:int)->object:
        if self.__onibus.pesquisar(poltrona) is None:
            raise OnibusException('Este assento está vazio.')

        return self.__onibus.pesquisar(poltrona)

    def exibirOnibus(self):
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
                    s += f'[{self.localizar(l, c).nome[:3].capitalize()}] '

            s+= '\n'

        temp = self.__linhas

        for j in range(self.__colunas):
            s += f'   {temp:^3}'
            temp += self.__linhas

        s += f'\n{self.__id}, {self.tamanho()-self.__onibus.unidades} assentos disponiveis.'

        return s


if __name__ == "__main__":
    path = str(Path(__file__).parent.resolve())+'/'
    onibusNome = "JPA-CG"
    contador = int()
    jpbus = Onibus(onibusNome,4,12)
    with open(str(path)+onibusNome+'.txt', 'a', encoding='utf-8') as f: 
        contador += 1
        f.write(f"Linha: {onibusNome}-{contador:0>3}\nPoltrona;passageiro;rg\n")
    
    onibusNome = "JPA-SP"
    jpbus = Onibus(onibusNome,4,12)
    with open(str(path)+onibusNome+'.txt', 'a', encoding='utf-8') as f: 
        contador += 1
        f.write(f"Linha: {onibusNome}-{contador:0>3}\nPoltrona;passageiro;rg\n")

    jpbus.alocar(Passageiro("samuel", "123"), 8)
    jpbus.alocar(Passageiro("madu", "456"), 9)
    jpbus.exibirOnibus()
    jpbus.trocarPoltrona(9, 10)
    jpbus.exibirOnibus()
    jpbus.desalocarPoltrona(8)
    jpbus.exibirOnibus()
    print(jpbus.retornarPoltrona("madu"))
    print(jpbus.retornarPassageiro(10))
    
"""
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