from abc import ABC, abstractmethod

class AbstractRegrasJogo(ABC):

    pass

def construir_jogo(*args,**kwargs):
    from jogo_classificacao import JogoClassificacaoLista

    return JogoClassificacaoLista()