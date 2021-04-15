import numpy as np
Gx=9
Gy=9

f = open ('map1010')
Map = [list(map(int,data.strip())) for data in f.readlines()]
f.close()
print("----Map----")
print (np.array(Map))


def next(queue,x,y,depth):
    if Map[x-1][y] < 1:
        queue.append([x-1,y,depth + 1])
    if Map[x+1][y] < 1:
        queue.append([x+1,y,depth + 1])
    if Map[x][y-1] < 1:
        queue.append([x,y-1,depth + 1])
    if Map[x][y+1] < 1:
        queue.append([x,y+1,depth + 1])

def maze():
    queue = [[1,1,2]]
    size=0
    time=0
    while len(queue)>0:
        if size < len(queue):
            size = len(queue)
        x,y,depth = queue.pop(0)
        if x == Gx and y == Gy:
            return depth
        Map[x][y] = depth
        next(queue,x,y,depth)
        time=time+1
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
    #print (np.array(Map))
    print("\n----Route----")
    print(np.array(route(result)))