class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def emitir_som(self):
        pass
    
class Mamifero(Animal):
    def amamentar(self):
        return f"O mamífero {self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"A ave {self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos."
    
morcego = Morcego(nome="Bruce")

# Acessando métodos da classe base `Animal`

print("Nome do morcego:", morcego.nome)  # Saída: Nome do morcego: Bruce   
print(morcego.emitir_som())  # Saída: Morcegos emitem sons ultrassônicos.

# Acessando métodos das classes `Mamifero` e `Ave`
print(morcego.amamentar())  # Saída: O mamífero Bruce está amamentando.
print(morcego.voar())  # Saída: A ave Bruce está voando.