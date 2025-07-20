class Lancamento:
    def __init__(self, descricao: str, valor: float, categoria: str):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def __repr__(self):
        return f"{self.__class__.__name__}({self.descricao}, R${self.valor:.2f}, {self.categoria})"