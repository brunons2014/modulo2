# POO


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    # Objetos
pessoa1 = Pessoa("Bruno", 30)
mensagem = pessoa1.saudacao()
print(mensagem)  # Saída: Olá, meu nome é Bruno e tenho 30 anos.

pessoa2 = Pessoa("Ana", 25)
print(pessoa2.saudacao())  # Saída: Olá, meu nome é Ana e tenho 25 anos.