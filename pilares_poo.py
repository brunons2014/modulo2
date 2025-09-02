#Exemplo de Herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} está andando.")
    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo:")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")
    
print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: R$ {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"saldo da conta bancária: R$ {conta.consultar_saldo()}")
conta.depositar(valor=-200)
print(f"saldo da conta bancária: R$ {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"saldo da conta bancária: R$ {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=500)
print(f"Saldo da conta do Zezinho: R$ {conta_do_zezinho.consultar_saldo()}")



#Exemplo de Abstração
print("\nExemplo de Abstração:")
from abc import ABC, abstractmethod

class veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
        
class Carro(veiculo):
    
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        print("O carro está ligado.")
        
    def desligar(self):
        print("O carro está desligado.")
        
carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())