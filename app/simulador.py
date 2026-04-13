def investimento(valor, taxa, tempo):
    return valor * (1 + taxa) ** tempo

def saldo(receitas, despesas):
    return sum(receitas) - sum(despesas)
