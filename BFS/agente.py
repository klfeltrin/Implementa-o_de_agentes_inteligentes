from movimentos import movimentos

class agente():
    def __init__(self, percepcao = None , acao = [] , movimentos = None ):
        self.movimentos = movimentos

        self.percepcao = percepcao
        self.acao = acao
        self.no = []   
        self.escolherProximaAcao() 
        pass
        

        if self.percepcao is not None:
            if ((self.estado_final())and
            (self.fim_de_jogo())):
                self.fim = True
            else:
                self.fim = False
       
    
    def adquirirPercepcao(self, percepcao_mundo):    
        self.percepcao = percepcao_mundo 
        for line in range(len(self.percepcao)):
            for colum in range(len(self.percepcao)) :
                if self.percepcao[line][colum] == '.':      
                    if colum < 5:
                        if (self.percepcao[line][colum + 1] == '.' and
                            self.percepcao[line][colum + 2]  == ','): 
                            self.no.append(agente(self.percepcao.copy() , [line, colum], movimentos.DIREITA ))    

                    if colum > 2 :
                        if (self.percepcao[line][colum - 1]== '.' and
                            self.percepcao[line][colum - 2] == ','):
                            self.no.append(agente(self.percepcao.copy() , [line, colum] , movimentos.ESQUERDA))    
                            
                    if line < 5:
                        if (self.percepcao[line + 1][colum] == '.' and
                            self.percepcao[line + 2][colum] == ',' ):
                            self.no.append(agente(self.percepcao.copy() , [line, colum] , movimentos.BAIXO))    
                            
                    if line > 2 :
                        if (self.percepcao[line - 1][colum]== '.' and
                            self.percepcao[line - 2][colum] == ',' ):
                            self.no.append(agente(self.percepcao.copy() , [line, colum] , movimentos.CIMA))    
        pass
        
    def escolherProximaAcao(self):    
        if self.movimentos == movimentos.DIREITA:
            line = list(self.percepcao[self.acao[0]])

            line[self.acao[1] + 1] = ','
            line[self.acao[1] + 2] = '.'
            line[self.acao[1]] = ','

            self.percepcao[self.acao[0]] = ''.join(line)

        elif self.movimentos == movimentos.ESQUERDA:
            line = list(self.percepcao[self.acao[0]])

            line[self.acao[1]] = ','
            line[self.acao[1] - 1] = ','
            line[self.acao[1] - 2] = '.'

            self.percepcao[self.acao[0]] = ''.join(line)

        elif self.movimentos == movimentos.BAIXO:
            for i in range(0, 3, 1):
                line = list(self.percepcao[self.acao[0] + i ])
               
                if i == 2 :line[self.acao[1]] = '.' 
                else: line[self.acao[1]] = ',' 

                self.percepcao[self.acao[0] + i] = ''.join(line)
        elif self.movimentos == movimentos.CIMA:
            for i in range(0, -3, -1):
                line = list(self.percepcao[self.acao[0] + i ])
               
                if i  == -2 :line[self.acao[1]] = '.' 
                else: line[self.acao[1]] = ',' 

                self.percepcao[self.acao[0] + i] = ''.join(line)


    def fim_de_jogo(self):
        for line in range(len(self.percepcao)):
            for colum in range(len(self.percepcao)) :
                if self.percepcao[line][colum] == '.':
                    if colum < 5:
                         if (self.percepcao[line][colum + 1] == '.' and
                            self.percepcao[line][colum + 2]  == ','): 
                            return False
                    if colum > 2 :
                        if (self.percepcao[line][colum - 1] == '.' and
                            self.percepcao[line][colum - 2]  == ','):
                            return False
                    if line < 5:
                        if (self.percepcao[line + 1][colum] == '.' and
                            self.percepcao[line + 2][colum] == ',' ):
                            return False
                    if line > 2 :
                        if (self.percepcao[line - 1][colum] == '.' and
                            self.percepcao[line - 2][colum] == ',' ):
                            return False                 
        return True

    def estado_final(self):
        retorno = False
        for line in self.percepcao:
            for colum in line :
                if colum == '.':
                    if retorno == True:
                        return False
                    else:
                        retorno = True 
        return True 
       
def construir_agente():
        
    return agente()
