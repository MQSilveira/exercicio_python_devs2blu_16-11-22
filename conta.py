class Conta:
    
    __titular = ''          # Atributos de Classe privados
    __numero = ''
    __saldo = ''
    
    # Dunder String
    def __str__(self):
        return f'{self.titular};{self.numero};{self.saldo}'
    
    
    # Properties / getter e setter
    @property
    def titular(self):
        return self.__titular.title()
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
