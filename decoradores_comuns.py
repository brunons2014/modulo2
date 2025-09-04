class MinhaClasse:
    valor = 10 # Atributo de classe
    
    def __init__(self, nome) -> None:
        self.nome = nome # Atributo de instância
        
    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Olá, {self.nome}! O valor é {self.valor}."
    
    @classmethod
    def metodo_classe(cls):
        return f"Este é um método de classe. O valor é {cls.valor}."
    
    @staticmethod
    def metodo_estatico():
        return "Este é um método estático. Não tem acesso a instância ou classe."
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())  # Chamada do método de instância
print(MinhaClasse.valor)  # Acesso ao atributo de classe
print(MinhaClasse.metodo_classe())  # Chamada do método de classe
print(MinhaClasse.metodo_estatico())  # Chamada do método estático

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split('-')
        return cls(marca, modelo, int(2022))
    
configuracao1 = "Toyota-Corolla-2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b    
    
print(Matematica.somar(5, 3))  # Saída: 8
print(Matematica.multiplicar(5, 3))  # Saída: