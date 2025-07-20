from models.gasto import Gasto
from models.receita import Receita

class FinanceiroChatbot:
    def __init__(self):
        self.transacoes = []

    def adicionar_gasto(self, descricao, valor, categoria):
        self.transacoes.append(Gasto(descricao, valor, categoria))

    def adicionar_receita(self, descricao, valor, categoria):
        self.transacoes.append(Receita(descricao, valor, categoria))

    def listar_transacoes(self):
        return self.transacoes

    def saldo_total(self):
        saldo = 0
        for t in self.transacoes:
            if isinstance(t, Receita):
                saldo += t.valor
            elif isinstance(t, Gasto):
                saldo -= t.valor
        return saldo

    def total_por_categoria(self):
        totais = {}
        for t in self.transacoes:
            sinal = 1 if isinstance(t, Receita) else -1
            totais[t.categoria] = totais.get(t.categoria, 0) + (sinal * t.valor)
        return totais
