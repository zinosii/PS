import sys,heapq
input=sys.stdin.readline


def e(p,q):
    if not q:
        return p
    return e(q,p%q)

n=int(input())
l=[]
for i in range(n-1):
    a,b,p,q=map(int,input().split())
    if a>b:
        t=a
        a=b
        b=t
        t=p
        p=q
        q=t
    x=e(p,q)
    p=p//x
    q=q//x
    l.append([a,b,p,q])
l.sort()

a=[[-1,-1] for _ in range(n)]
a[0]=[1,1]
p=1
v=[0]*n
v[0]=1

while l:
    for i in l:
        x=i[0]
        y=i[1]
        if v[y]:
            a[x][0]=a[y][0]*i[2]
            a[x][1]=a[y][1]*i[3]
            v[x]=1
            p*=i[3]
            l.remove(i)
            break
        elif v[x]:
            a[y][0]=a[x][0]*i[3]
            a[y][1]=a[x][1]*i[2] 
            v[y]=1
            p*=i[2]
            l.remove(i)
            break
        else:
            continue

ll=[]
for i in a:
    ll.append(i[0]*p//i[1])

g=1
for i in range(2,11):
    for j in range(10):
        g*=i
for i in ll:
    g=e(g,i)

for i in ll:
    print(i//g,end=' ')
