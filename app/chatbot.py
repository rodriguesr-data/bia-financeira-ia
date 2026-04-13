from simulador import investimento, saldo
from contexto import salvar, obter

def responder(pergunta):
    pergunta = pergunta.lower()

    if "simular investimento" in pergunta:
        try:
            valor = float(input("Valor: "))
            taxa = float(input("Taxa (ex: 0.1): "))
            tempo = int(input("Tempo (anos): "))

            resultado = investimento(valor, taxa, tempo)
            salvar("ultimo_investimento", resultado)

            return f"Valor final: R${resultado:.2f}"
        except:
            return "Erro na simulação. Verifique os valores."

    elif "investimento" in pergunta:
        return "Digite: simular investimento"

    elif "saldo" in pergunta:
        try:
            receitas = list(map(float, input("Receitas (separadas por espaço): ").split()))
            despesas = list(map(float, input("Despesas (separadas por espaço): ").split()))

            resultado = saldo(receitas, despesas)
            return f"Saldo: R${resultado:.2f}"
        except:
            return "Erro ao calcular saldo."

    elif "cdb" in pergunta:
        return "CDB é um investimento de renda fixa emitido por bancos."

    elif "poupança" in pergunta or "poupanca" in pergunta:
        return "Poupança é um investimento simples, porém com baixo rendimento."

    elif "ultimo investimento" in pergunta:
        ult = obter("ultimo_investimento")
        if ult:
            return f"Último investimento: R${ult:.2f}"
        else:
            return "Nenhum investimento realizado ainda."

    else:
        return "Pergunte sobre investimentos, saldo ou produtos financeiros."
