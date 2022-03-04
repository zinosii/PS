import sys
input=sys.stdin.readline

R,C=map(int,input().split())
Board=[list(map(int,input().rstrip())) for _ in range(R)]

DP=[[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        DP[i][j]=Board[i][j]
m=0        
for i in range(R-1):
    for j in range(C-1):
        if DP[i][j] and DP[i][j+1] and DP[i+1][j] and DP[i+1][j+1]:
            DP[i+1][j+1]=min(DP[i][j],DP[i+1][j],DP[i][j+1])+1
            
for i in range(R):
    for j in range(C):
        m=max(m,DP[i][j])

print(m*m)



