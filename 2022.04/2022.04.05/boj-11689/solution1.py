import sys
input=sys.stdin.readline
N=int(input())
if N==1:
    print(1)
    exit(0)
n=int(N**(1/2))+1
p=[1]*(n+1)
p[0]=0
p[1]=0
Primes=[] #루트N 이하의 소수 리스트
for i in range(2,n+1):
    if p[i]:
        Primes.append(i)
    for j in Primes:
        if i*j>n:
            break
        p[i*j]=0
        if not i%j:
            break

def isprime(x):
    for i in Primes:
        if not x%i:
            return 0
    return 1

def f(x):
    if x==1:
        return []
    if isprime(x):
        return [x]
    for i in Primes:
        if not x%i:
            while not x%i:
                x//=i
            return [i]+f(x)
        
plist=f(N)
l=len(plist)

def h(idx,m,n,s):
    global ret
    if idx==m:
        t=1
        for i in n:
            t*=i
        ret.append(t)
        return
    for i in range(s,l):
        if plist[i] not in n:
            n.append(plist[i])
            h(idx+1,m,n,i)
            n.pop()
    return ret
    
def g(m):
    global ret
    ret=[]
    return h(0,m,[],0) #m개를 고른것 = (l,m)

ans=N
for i in range(1,l+1):
    if i%2:
        for j in g(i):
            ans-=N//j
    else:
        for j in g(i):
            ans+=N//j 
print(ans)
