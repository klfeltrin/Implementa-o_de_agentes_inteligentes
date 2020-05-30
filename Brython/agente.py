from browser.template import Template
from browser import alert, document, console, timer

class agente():
    def __init__(self):
        self.percepcao = None
        self.no = []         
        pass
    
    def adquirirPercepcao(self, percepcao_mundo):     
        
        self.percepcao = percepcao_mundo 
        pass
        
    def escolherProximaAcao(self):
        linha = self.percepcao.children
        for line in range(len(linha)):
            for colum in range(len(linha)) :
                if linha[line].children[colum].innerText == '.':      
                    if colum < 5:
                        if (linha[line].children[colum + 1].innerText == '.' and
                            linha[line].children[colum + 2].innerText  == ','): 
                            return [line , colum] 
                    if colum > 2 :
                        if (linha[line].children[colum - 1].innerText == '.' and
                            linha[line].children[colum - 2].innerText  == ','):
                            return [line , colum] 
                    if line < 5:
                        if (linha[line + 1].children[colum].innerText == '.' and
                            linha[line + 2].children[colum].innerText == ',' ):
                            return [line , colum] 
                    if line > 2 :
                        if (linha[line -1].children[colum].innerText == '.' and
                            linha[line - 2].children[colum].innerText == ',' ):
                            return [line , colum] 
        pass

    def construir_agente():
        
        return agente()


