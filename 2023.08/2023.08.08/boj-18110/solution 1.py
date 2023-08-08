import sys
input=sys.stdin.readline

N=int(input())
s=[]
for i in range(N):
    s.append(int(input()))
            

s.sort()
if N%20:
    if 3*N/20-int(3*N/20)>=0.5:
        t=int(3*N/20)+1
    else:
        t=int(3*N/20)
else:
    t=int(N*0.15)

if N:
    s=s[t:len(s)-t]
    k=sum(s)/len(s)
    if sum(s)%len(s):
        if k-int(k)>=0.5:
            print(int(k)+1)
        else:
            print(int(k))
    else:
        print(int(k))
else:
    print(0)