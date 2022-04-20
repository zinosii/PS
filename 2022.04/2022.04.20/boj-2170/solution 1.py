import sys,heapq
from collections import deque
input=sys.stdin.readline

N=int(input())
h=[]
for i in range(N):
    heapq.heappush(h,map(int,input().split()))
ans=0
print(h)
s,e=heapq.heappop(h)
while h:
    ts,te=heapq.heappop(h)
    if ts<=e:
        if te>e:
            e=te
    else:
        ans+=e-s
        s=ts
        e=te
    print(ts,te,s,e,ans)
ans+=e-s
print(ans)
    
