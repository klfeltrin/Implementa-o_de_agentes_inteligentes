from regras_jogo.regras_abstratas import construir_jogo

def iniciar_jogo():
    jogo = construir_jogo()

    for i in jogo.tabuleiro:
        print(i)

    return jogo
        

if __name__ == "__main__":
    iniciar_jogo()
    pass