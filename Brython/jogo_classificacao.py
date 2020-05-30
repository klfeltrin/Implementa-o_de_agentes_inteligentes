from regras_abstratas import AbstractRegrasJogo
import sys

from browser.html import A, DIV, BR, TABLE, TD, TR, BUTTON
from browser.template import Template
from browser import alert, document, console, timer



class JogoClassificacaoLista(AbstractRegrasJogo):

    def __init__(self):

        self.tabuleiro = [
            '  ...  ',
            '  ...  ',
            '.......',
            '...,...',
            '.......',
            '  ...  ',
            '  ...  '
        ]  
    '''
        self.tabuleiro = [
            '  ,,,  ',
            '  ,,,  ',
            ',,,,,,,',
            ',,,.,,,',
            ',,,.,,,',
            '  ,,,  ',
            '  ,,,  '
        ]  
    '''

    def isFim(self):
        for line in range(len(self.tabuleiro)):
            for colum in range(len(self.tabuleiro)) :
                if self.tabuleiro[line][colum] == '.':
                    if colum < 5:
                         if (self.tabuleiro[line][colum + 1] == '.' and
                            self.tabuleiro[line][colum + 2]  == ','): 
                            return True
                    if colum > 2 :
                        if (self.tabuleiro[line][colum - 1] == '.' and
                            self.tabuleiro[line][colum - 2]  == ','):
                            return True 
                    if line < 5:
                        if (self.tabuleiro[line + 1][colum] == '.' and
                            self.tabuleiro[line + 2][colum] == ',' ):
                            return True
                    if line > 2 :
                        if (self.tabuleiro[line - 1][colum] == '.' and
                            self.tabuleiro[line - 2][colum] == ',' ):
                            return True
        return False

                
        '''retorno = False
        for line in self.tabuleiro:
            for colum in line :
                if colum == '.':
                    if retorno == True:
                        return False
                    else:
                        retorno = True 
        return True  
        ''' 

    def registrarProximaAcao(self, acao_line, acao_colum):
        self.acao  =  [int(acao_line) , int(acao_colum)] 
        pass 

    def atualizarEstado(self):
        if self.validacao[0]:
            line = list(self.tabuleiro[self.acao[0]])

            line[self.acao[1]] = ','
            line[self.acao[1] - 1] = ','
            line[self.acao[1] - 2 ] = '.'

            self.tabuleiro[self.acao[0]] = ''.join(line)
            return
            
        if self.validacao[1]:
            line = list(self.tabuleiro[self.acao[0]])

            line[self.acao[1]] = ','
            line[self.acao[1]+ 1] = ','
            line[self.acao[1]+ 2] = '.'

            self.tabuleiro[self.acao[0]] = ''.join(line)   
            
            return

        if self.validacao[2]:
            for i in range(0 , -3, -1):
                line = list(self.tabuleiro[self.acao[0] + i ])
               
                if i  == (-2) : line[self.acao[1]] = '.' 
                else: line[self.acao[1]] = ',' 

                self.tabuleiro[self.acao[0] + i] = ''.join(line)
            return     

        if self.validacao[3]:
            for i in range(0, 3, 1):
                line = list(self.tabuleiro[self.acao[0] + i ])
               
                if i  == 2 :line[self.acao[1]] = '.' 
                else: line[self.acao[1]] = ',' 

                self.tabuleiro[self.acao[0] + i] = ''.join(line)
            return  
        pass

    def validarEstado(self):
        self.validacao = [False, False, False, False]

        if (((self.tabuleiro[self.acao[0]][self.acao[1] - 1] == '.' ) and 
        (self.tabuleiro[self.acao[0]][self.acao[1] - 2] == ',' )) and
        ((self.acao[1] - 2) > 0)):
            
            self.validacao[0]  = True

            pass

        if(((self.acao[1] + 2) < 7) and
        ((self.tabuleiro[self.acao[0]][self.acao[1] + 1] == '.' ) and 
        (self.tabuleiro[self.acao[0]][self.acao[1] + 2] == ',' ))):
            
            self.validacao[1]  = True

            pass    

        if(((self.tabuleiro[self.acao[0]- 1][self.acao[1]] == '.' ) and 
        (self.tabuleiro[self.acao[0]- 2][self.acao[1]] == ',' )) and
        ((self.acao[0] - 2) > 0)):
            
            self.validacao[2]  = True
            
            pass

        if(((self.acao[0] + 2) < 7 ) and
        ((self.tabuleiro[self.acao[0]+ 1][self.acao[1]] == '.' ) and 
        (self.tabuleiro[self.acao[0]+ 2][self.acao[1]] == ',' ))):
            
            self.validacao[3]  = True
            
            pass





