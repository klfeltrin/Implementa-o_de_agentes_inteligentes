import sys
from browser.timer import request_animation_frame as raf
from browser.timer import cancel_animation_frame as caf

from browser.html import A, DIV, BR, TABLE, TD, TR, BUTTON
from browser.template import Template
from browser import alert, document, console, timer

from regras_abstratas import construir_jogo
from agente import agente
from collections import Counter

def gerarCampoVisao(tabuleiro):
    document['tabelajogo'].clear()

    def hovertrueposition(event):
        event.target.style.background = 'rgba(0, 255, 0, 0.3)'

    def hoverfalseposition(event):   
        event.target.style.background = 'rgba(255, 0, 0, 0.3)'

    def hoverleaveposition(event):      
        event.target.style.background = ''

    def toast(event):
        new = DIV(event.path[2].id + " / " + event.path[1].id, Class='toast')
        document['desenv'] <= new

        def hidden():
            new.style.display = 'none'
            
        timer.set_timeout(hidden, 3000)

    jogo = TABLE(Class="jogo")
        
    for line in range(7):
        aux = ''

        for coluna in range(7):  
            if tabuleiro[line][coluna] == '.' :
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incr).bind('click', toast), id=coluna
                    ).bind('mouseenter',hovertrueposition).bind('mouseleave',hoverleaveposition)
            else:
                aux += TD(A({tabuleiro[line][coluna]}).bind('click', toast), id=coluna
                    ).bind('mouseenter',hoverfalseposition).bind('mouseleave',hoverleaveposition)
     
        jogo <= TR(aux, id=line)
        aux = ""

    return jogo

def gerarCampoDePossibilidades(tabuleiro):
    document['tabelajogo'].clear()

    tabela = TABLE(Class="jogo")
        
    for line in range(7):
        aux = ''

        for coluna in range(7):  
            if (jogo.acao[0] == line and jogo.acao[1] == coluna):
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incrlog), Class='acao')

            elif (jogo.acao[0] == line and (jogo.acao[1]-2) == coluna and jogo.validacao[0]) :
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incrlog), id=0, Class='possibilidade')

            elif (jogo.acao[0] == line and (jogo.acao[1]+2 )== coluna and jogo.validacao[1]) :
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incrlog), id=1, Class='possibilidade')

            elif ((jogo.acao[0]-2) == line and jogo.acao[1] == coluna and jogo.validacao[2]) :
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incrlog), id=2, Class='possibilidade')  

            elif ((jogo.acao[0]+2) == line and jogo.acao[1] == coluna and jogo.validacao[3]) :
                aux += TD(A({tabuleiro[line][coluna]}).bind('click',incrlog), id=3, Class='possibilidade') 

            else : 
                aux += TD(A({tabuleiro[line][coluna]}))
            
        tabela <= TR(aux, id=line)
        aux = ""

    return tabela    

def incrlog(event):
    for i in range(len(jogo.validacao)):
        if i != int(event.path[1].id):
            jogo.validacao[i] = False

    jogo.atualizarEstado()
    document['tabelajogo'] <= gerarCampoVisao(jogo.tabuleiro)

def incr(event):
   
    jogo.registrarProximaAcao(event.path[2].id, event.path[1].id)

    jogo.validarEstado()

    if dict(Counter(jogo.validacao))[True] > 1:
        document['tabelajogo'] <= gerarCampoDePossibilidades(jogo.tabuleiro)

    else:
        jogo.atualizarEstado()
        document['tabelajogo'] <= gerarCampoVisao(jogo.tabuleiro)

        if not jogo.isFim():
            alert('O jogo Acabou')

def jogador_agente():
    document['tabelajogo'] <= gerarCampoVisao(jogo.tabuleiro)

    agente_jogador.adquirirPercepcao(gerarCampoVisao(jogo.tabuleiro))
    acao = agente_jogador.escolherProximaAcao()

    if acao is not None:
        jogo.registrarProximaAcao(acao[0], acao[1])

        jogo.validarEstado()
        jogo.atualizarEstado()
    else:
        alert("fim")
        caf(id)

def animate(i):

    global id
    id = raf(animate)
    jogador_agente()
    document['tabelajogo'] <= gerarCampoVisao(jogo.tabuleiro)

jogo = construir_jogo()
#linha toast 
document <= DIV('', Class='desenv', id='desenv')
#linha jogo
agente_jogador = agente()

document['tabelajogo'] <= gerarCampoVisao(jogo.tabuleiro)

document['btn-animate'].bind('click', animate)   



    


