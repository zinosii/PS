import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
idx=[-1]*n
s=[]
order=1
for i in l:
    while s and s[-1][0] < i:
        idx[s[-1][1]-1]=i
        s.pop()
    s.append((i,order))
    order+=1
for i in idx:
    print(i,end=' ')
