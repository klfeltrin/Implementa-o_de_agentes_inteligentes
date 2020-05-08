from browser.html import  DIV, BR, TABLE, TD, TR, A

tabuleiro = [
    "  ...  ",
    "  ...  ",
    ".......",
    "...,...",
    ".......",
    "  ...  ",
    "  ...  "
    ]

def jogo():
    jogo = TABLE(Class="jogo")
    aux = ""
    for line in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[line])):
            aux += TD(A(tabuleiro[line][coluna],onclick='celula()'), value=coluna)
        jogo <= TR(aux, value=line)
        aux = ""
    return jogo