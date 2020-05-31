import sys

from agente import construir_agente
from regras_abstratas import construir_jogo

sys.setrecursionlimit(5000)

agente_raiz = construir_agente()
jogo = construir_jogo()

lista_no = []

agente_raiz.adquirirPercepcao(jogo.tabuleiro)

for i in range (3):
    agente_raiz.no.pop(1)


for i in agente_raiz.no:
    i.adquirirPercepcao(i.percepcao)
    for um in i.no:
        if um.fim is not True:
            lista_no.append(um)
        else:
            for u in um.percepcao :
                for t in u:
                    print(t)    
agente_raiz.no = lista_no
lista_no = [] 

agente_raiz.no.pop(1)




def busca(agente_param):
    for i in agente_param.no:
        i.adquirirPercepcao(i.percepcao)
        if len(i.no) > 0:
            busca(i)
        else:
            for j in i.percepcao:
                print(j)
            print()






busca(agente_raiz)

print ("fim")
