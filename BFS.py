import numpy as np
import glob
Gx=99
Gy=99

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
    size=[0,0]
    while len(queue)>0:
        if size[0] < len(queue):
            size[0] = len(queue)
        x,y,depth = queue.pop(0)
        if x == Gx and y == Gy:
            #print('maxsize='+str(size[0]))
            #print('O='+str(size[1]))
            return size
        Map[x][y] = depth
        next(queue,x,y,depth)
        size[1]=size[1]+1
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
    #[max, ave, min]
    #result[0]=size, [1]=time
    size=[0,0,100000000]
    sizevar=[]
    time=[0,0,100000000]
    timevar=[]
    Maps= glob.glob("./6045/*")
    for Map in Maps:
        #print(Map)
        with open (Map,'r',encoding='utf-8')as f:
            Map = [list(map(int,data.strip())) for data in f.readlines()]
        f.close()
        result=maze()
        if size[0] < result[0]: #Max
            size[0] = result[0]
        if time[0] < result[1]:
            time[0] = result[1]
        if size[2] > result[0]:
            size[2] = result[0]
        if time[2] >result[1]:
            time[2] = result[1]
        sizevar.append(result[0])
        timevar.append(result[1])
        size[1]+=result[0]
        time[1]+=result[1]
print("#BFS#")
print("----Time----")
print("Max="+str(time[0])+"\n"+"Min="+str(time[2])+"\n"+"Ave="+str(time[1]/100))
print("var="+str(np.var(timevar)))
print("std="+str(np.var(timevar)**0.5))
print("----Size----")
print("Max="+str(size[0])+"\n"+"Min="+str(size[2])+"\n"+"Ave="+str(size[1]/100))
print("var="+str(np.var(sizevar)))
print("std="+str(np.var(sizevar)**0.5))