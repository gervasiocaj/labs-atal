# coding: utf-8
from sys import stdout

def main():
    route = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    printRoute(route)
    # the result will be [ (0,0), (1,0), (1,1), (2,1), (3,1), (3,2), (3,3) ]
    
    route = [[1, 1], [1, 1]]
    printRoute(route)
    
    route = [[1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 1, 1]]
    printRoute(route)
    

def findPath(route, track = [], pos = (0,0)): #backtracking
    # se a posição é válida, marque a casa atual da matriz de solução como 1
    if route[pos[0]][pos[1]] == 1:
        track = track + [pos]
    else:
        return
    
    if pos == (len(route)-1, len(route)-1) : # se o destino foi acançado
        # imprima a matriz de solução
        print 'found possible track: ', track
        
    else:
        # mova para a direita e recursivamente verifique se uma solução foi alcançada.
        posRight = (pos[0], pos[1]+1)
        if (validPos(posRight, route)):
            findPath(route, track, posRight)
        
        # se uma solução não foi alcançada, tente o mesmo movendo para baixo.
        posDown = (pos[0]+1, pos[1])
        if (validPos(posDown, route)):
            findPath(route, track, posDown)
        
def validPos(pos, route):
    return pos[0] <= len(route) -1 and pos[1] <= len(route)-1
    
def printRoute(route):
    print 'route = ', route, '\n'
    for row in route:
        for col in row:
            stdout.write('_' if col == 1 else 'x')
        print ''
    print ''
    findPath(route)
    print '\n---\n'


main()