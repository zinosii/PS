import sys,heapq
input=sys.stdin.readline

n=int(input())

l=[]
for i in range(n):
    t=list(map(int,input().split('.')))
    for i in range(4):
        x=format(t[i],"b")
        while len(x)!=8:
            x='0'+x
        t[i]=x
    l.append(t)


f=0
for idx in range(4):
    c=l[0][idx]
    for i in range(n):
        if c!=l[i][idx]:
            f=1
            break
    if f:
        break

f=0
for idx2 in range(8):
    c=l[0][idx][idx2]
    for i in range(n):
        if c!=l[i][idx][idx2]:
            f=1
            break
    if f:
        break
if not f and idx2==7:
    idx2=8
add=[]
mask=[]
for i in range(idx):
    add.append(l[0][i])
    mask.append("11111111")
addtemp=""
masktemp=""
for i in range(idx2):
    addtemp+=str(l[0][idx][i])
    masktemp+="1"
while len(addtemp)!=8:
    addtemp+="0"
    masktemp+="0"
add.append(addtemp)
mask.append(masktemp)
for i in range(3-idx):
    add.append("00000000")
    mask.append("00000000")

cnt=0
for i in add:
    print(int(i,2),end='')
    if cnt<3:
        print('.',end='')
    cnt+=1
print()
cnt=0
for i in mask:
    print(int(i,2),end='')
    if cnt<3:
        print('.',end='')
    cnt+=1
