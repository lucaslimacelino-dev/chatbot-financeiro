from models.lancamento import Lancamento

class Gasto(Lancamento):
    def __init__(self, descricao: str, valor: float, categoria: str):
        super().__init__(descricao, valor, categoria)