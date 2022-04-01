import sys
input=sys.stdin.readline


def stn(x): #문자를 숫자로
    ret=0
    for i in range(len(x)):
        if '0'<=x[i]<='9':
            ret+=(ord(x[i])-48)*(36**(len(x)-i-1))
        else:
            ret+=(ord(x[i])-55)*(36**(len(x)-i-1))
    return ret

def nts(x): #숫자를 문자로
    if x==0: #반례, 0이 입력되면 0을 리턴해야함...
        return ['0']
    ret=[]
    while x:
        if x%36>=10:
            ret.append(chr(x%36+55))
        else:
            ret.append(x%36)
        x//=36
    return(ret[::-1])



N=int(input())
s=[] #문자들을 담을 리스트
for i in range(N):
    s.append(input().rstrip())
K=int(input())

d={i:[] for i in range(36)} #각 문자가 어느위치에 나오는지 저장함
for i in s:
    for j,k in enumerate(i):
        if '0'<=k<='9':
            d[ord(k)-48].append(len(i)-j-1)
        else:
            d[ord(k)-55].append(len(i)-j-1)
x=[0]*36 #각 문자가 Z로 바뀌었을때, 추가되는값들
for i in d:
    for j in d[i]:
        x[i]+=(35-i)*(36**j)
ans=0 #처음 값들의 합
for i in s:
    ans+=stn(i)

x.sort() 
x.reverse() #Z로 바뀌었을때 가장 크게 증가한 K개의 값을 더해주기 위해 sorting

for i in range(K):
    ans+=x[i]
    
for i in nts(ans):
    print(i,end='')
