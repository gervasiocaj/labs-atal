# coding: utf-8

def main():
    print 'main'
    
def backtracking():
    if True: #todas as casas foram visitadas
        #imprima o caminho
        return True
    else:
        #Adicione recursivamente o próximo movimento ao vetor
        #Se o movimento escolhido não satisfaz as condições do problema, remova o movimento do vetor e volte ao passo a)
        #Se nenhuma das alternativas funcionar, retorne falso
        return False
