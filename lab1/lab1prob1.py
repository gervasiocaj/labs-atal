# coding: utf-8

import random
import pprint

def main():
    inicio = (random.randint(0,7), random.randint(0,7))
    print passeio(inicio)
    
def passeio(posicao = (0,0), number = 0, tabuleiro = [[None for i in range(8)] for j in range(8)]):
    print tabuleiro
    if (True not in [None in i for i in tabuleiro]): #todas as casas foram visitadas
        print 'fim'
        printTabuleiro(tabuleiro)
        return True
    else:
        number += 1
        posA = posicao[0]
        posB = posicao[1]
        
        if noTabuleiro((posA+1, posB+2)): #1h
            if desocupada((posA+1, posB+2), tabuleiro):
                tabuleiro[posA+1][posB+2] = number
                passeio((posA+1, posB+2), number, tabuleiro)
                
        elif noTabuleiro((posA+2, posB+1)): #2h
            if desocupada((posA+2, posB+1), tabuleiro):
                tabuleiro[posA+2][posB+1] = number
                passeio((posA+2, posB+1), number, tabuleiro)
                
        elif noTabuleiro((posA+2, posB-1)): #4h
            if desocupada((posA+2, posB-1), tabuleiro):
                tabuleiro[posA+2][posB-1] = number
                passeio((posA+2, posB-1), number, tabuleiro)
                
        elif noTabuleiro((posA+1, posB-2)): #5h
            if desocupada((posA+1, posB-2), tabuleiro):
                tabuleiro[posA+1][posB-2] = number
                passeio((posA+1, posB-2), number, tabuleiro)
                
        elif noTabuleiro((posA-1, posB-2)): #7h
            if desocupada((posA-1, posB-2), tabuleiro):
                tabuleiro[posA-1][posB-2] = number
                passeio((posA-1, posB-2), number, tabuleiro)
                
        elif noTabuleiro((posA-2, posB-1)): #8h
            if desocupada((posA-2, posB-1), tabuleiro):
                tabuleiro[posA-2][posB-1] = number
                passeio((posA-2, posB-1), number, tabuleiro)
                
        elif noTabuleiro((posA-2, posB+1)): #10h
            if desocupada((posA-2, posB+1), tabuleiro):
                tabuleiro[posA-2][posB+1] = number
                passeio((posA-2, posB+1), number, tabuleiro)
                
        elif noTabuleiro((posA-1, posB+2)): #11
            if desocupada((posA-1, posB+2), tabuleiro):
                tabuleiro[posA-1][posB+2] = number
                passeio((posA-1, posB+2), number, tabuleiro)
                
        else:
            return False
        
        #Adicione recursivamente o próximo movimento ao vetor
        #Se o movimento escolhido não satisfaz as condições do problema, remova o movimento do vetor e volte ao passo a)
        #Se nenhuma das alternativas funcionar, retorne falso

def noTabuleiro(posicao):
    return (posicao[0] >= 0 and posicao[0] <= 7 and posicao[1] >= 0 and posicao[1] <= 7) or posicao[0] == None or posicao
    
def desocupada(posicao, tabuleiro):
    return tabuleiro[posicao[0]][posicao[1]] == None

def printTabuleiro(tabuleiro):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tabuleiro)

main()