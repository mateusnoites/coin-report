class BitcoinSummary():
    preco_atual: float
    diferenca_percentual: float
    preco_ontem: float
    condicao: str

    def __init__(self, preco_atual: float, diferenca: float, diferenca_percentual: float):
        self.preco_atual = preco_atual
        self.diferenca_percentual = diferenca_percentual
        self.preco_ontem = preco_atual - diferenca

        self.condicao = "alta" if diferenca_percentual > 0 else "queda"

    def abs_porcentagem(self):
        return round(abs(self.diferenca_percentual), 2)

    def formatar(self, valor: float):
        novo_valor = f"{valor:,.2f}"
        novo_valor = novo_valor.replace(',', 'X').replace('.', ',').replace('X', '.')
        return novo_valor