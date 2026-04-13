contexto = {}

def salvar(chave, valor):
    contexto[chave] = valor

def obter(chave):
    return contexto.get(chave)
