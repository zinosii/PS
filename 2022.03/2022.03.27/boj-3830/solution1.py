import sys,math
sys.setrecursionlimit(100000)
input=sys.stdin.readline

p=[]
W=[]
level=[]

def find(x):
    global p,W
    if x==p[x]:
        return x
    t=find(p[x])
    W[x]+=W[p[x]]
    p[x]=t
    return p[x]

def union(x,y,z):
    global W,p,level
    xx=find(x)
    yy=find(y)
    if xx!=yy:
        p[yy]=xx
        W[yy]=W[x]-W[y]+z
    
def f(N,M):
    global p,W,level
    p=[i for i in range(N+1)]
    W=[0]*(N+1)
    level=[0]*(N+1)
    for i in range(M):
        l=list(input().split())
        if l[0]=='!':
            a=int(l[1])
            b=int(l[2])
            w=int(l[3])
            union(a,b,w) 
        else:
            a=int(l[1])
            b=int(l[2])
            if find(a)!=find(b):
                print('UNKNOWN')
            else:
                print(W[b]-W[a])
        #print(p,W,level)
        
a,b=map(int,input().split())
while a!=0:
    f(a,b)
    a,b=map(int,input().split())
    
