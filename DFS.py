import numpy as np

Gx=9
Gy=9

f = open ('Map1010')
Map = [list(map(int,data.strip())) for data in f.readlines()]
f.close()
print (np.array(Map))


def next(stack,x,y,depth):
    if Map[x-1][y] < 1:
        stack.append([x-1,y,depth + 1])
    if Map[x+1][y] < 1:
        stack.append([x+1,y,depth + 1])
    if Map[x][y-1] < 1:
        stack.append([x,y-1,depth + 1])
    if Map[x][y+1] < 1:
        stack.append([x,y+1,depth + 1])

def maze():
    stack = [[1,1,2]]
    while len(stack)>0:
        x,y,depth = stack.pop()
        Map[x][y] = depth
        if x == Gx and y == Gy:
            return depth
        next(stack,x,y,depth)
    return 'false'

def route(depth):
    x=Gx
    y=Gy
    route=[[x,y]]
    while x!=1 or y!=1:
        if Map[x-1][y]==depth-1:
            route.append([y,x-1])
            x=x-1
            depth=depth-1
            Map[x][y]=0
        elif Map[x+1][y]==depth-1:
            route.append([y,x+1])
            x=x+1
            depth=depth-1
            Map[x][y]=0
        elif Map[x][y-1]==depth-1:
            route.append([y-1,x])
            y=y-1
            depth=depth-1
            Map[x][y]=0
        elif Map[x][y+1]==depth-1:
            route.append([y+1,x])
            y=y+1
            depth=depth-1
            Map[x][y]=0
    route.reverse()
    return route

if __name__ == '__main__':
    result=maze()
    np.set_printoptions(threshold=np.inf)
    print (np.array(Map))
    print(np.array(route(result)))