from agente import construir_agente
from regras_abstratas import construir_jogo

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


#bfs
while len(agente_raiz.no) > 0: 
    print(len(agente_raiz.no))
    for i in agente_raiz.no:
        i.adquirirPercepcao(i.percepcao)
        for um in i.no:
            if um.fim is not True:
                lista_no.append(um)
            else:
                for u in um.percepcao :
                    print(u)  
                print()
    agente_raiz.no = lista_no
    lista_no = []  





for i in agente_raiz.no:
    for j in i.percepcao:
        print(j)
    print()

