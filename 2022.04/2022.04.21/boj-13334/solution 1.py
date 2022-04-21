import sys,heapq
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
d=int(input())
ll=[]
for i in l:
    if abs(i[0]-i[1])<=d:
        t=sorted(i)
        ll.append(t)
ll.sort(key=lambda x:x[1])

ans=0
h=[]
for i in ll:
    if not h:
        h=[i]
    else:
        while h[0][0]<i[1]-d:
            heapq.heappop(h)
            if not h:
                break
        heapq.heappush(h,i)
    ans=max(ans,len(h))

print(ans)
