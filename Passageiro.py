class Passageiro:
    def __init__(self, nome:str, rg:str):
        self.__nome = nome
        self.__rg = rg
    
    @property
    def nome(self)->str:
        return self.__nome

    def __str__(self):
        return f'{self.__nome} RG {self.__rg}'
