from simulador import investimento, saldo
from contexto import salvar, obter

def responder(pergunta):
    pergunta = pergunta.lower()

    if "investimento" in pergunta:
        return "Digite: simular investimento"

    elif "simular investimento" in pergunta:
        valor = float(input("Valor: "))
        taxa = float(input("Taxa (ex: 0.1): "))
        tempo = int(input("Tempo (anos): "))

        resultado = investimento(valor, taxa, tempo)
        salvar("ultimo_investimento", resultado)

        return f"Valor final: R${resultado:.2f}"

    elif "saldo" in pergunta:
        receitas = list(map(float, input("Receitas: ").split()))
        despesas = list(map(float, input("Despesas: ").split()))

        resultado = saldo(receitas, despesas)
        return f"Saldo: R${resultado:.2f}"

    elif "cdb" in pergunta:
        return "CDB é um investimento de renda fixa."

    elif "ultimo" in pergunta:
        ult = obter("ultimo_investimento")
        return f"Último investimento: R${ult:.2f}" if ult else "Nenhum ainda."

    else:
        return "Pergunte sobre investimentos ou saldo."
