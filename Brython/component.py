import sys

from browser.html import A, DIV, BR, TABLE, TD, TR, BUTTON
from browser.template import Template
from browser import alert, document, console, timer

from regras_abstratas import construir_jogo

def jogon(tabuleiro):
    jogo = TABLE(Class="jogo")
    
    for line in range(7):
        aux = ''

        for coluna in range(7):
            aux += TD(A({tabuleiro[line][coluna]}).bind('click',incr).bind('click', toast), id=coluna)
       
        jogo <= TR(aux, id=line)
        aux = ""

    return jogo

def incr(event):
    line = list(jogo.tabuleiro[int(event.path[2].id)])
    line[int(event.path[1].id)] = ','

    jogo.tabuleiro[int(event.path[2].id)] = ''.join(line)
    document['tabelajogo'].clear()

    document['tabelajogo'] <= jogon(jogo.tabuleiro)

def toast(e):
    new = DIV(e.path[2].id + " / " + e.path[1].id, Class='toast')
    document['desenv'] <= new

    def hidden():
        new.style.display = 'none'

    timer.set_timeout(hidden, 3000)

jogo = construir_jogo()

document <= DIV('', Class='desenv', id='desenv')
document['tabelajogo'] <= jogon(jogo.tabuleiro)
