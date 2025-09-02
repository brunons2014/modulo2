def meu_decorador(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada.")
    
minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da execução da função1.")
        resultado = self.func()
        print("Depois da execução da função1.")
        return resultado
    
@MeuDecoradorDeClasse
def segunda_funcao():
    print("Minha função 2 foi chamada.")
    
segunda_funcao()