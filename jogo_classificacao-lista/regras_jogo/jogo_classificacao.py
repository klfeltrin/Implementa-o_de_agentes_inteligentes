from regras_jogo.regras_abstratas import AbstractRegrasJogo

class JogoClassificacaoLista(AbstractRegrasJogo):

    def __init__(self):

        self.tabuleiro = [
            "  ...  ",
            "  ...  ",
            ".......",
            "...,...",
            ".......",
            "  ...  ",
            "  ...  "
        ]         
