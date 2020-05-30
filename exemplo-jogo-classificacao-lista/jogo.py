#!/usr/bin/env python3

import time
from regras_jogo.regras_abstratas import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.O_JOGADOR)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
                
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        tempo_corrente = time.time()
        jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += tempo_corrente

    jogo.terminarJogo()

if __name__ == '__main__':
    iniciar_jogo()