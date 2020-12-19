# 4-1
n=int(input())
for i in range(n+1):
    print("pow(3,%d) = %d"%(i,pow(3,i)))
    
# 4-2
m,n=map(int,input().split())
sum = 0
count = 0
if m==1:
    m+=1
for i in range(m,n+1):
    for k in range(2,i):
        if i%k==0:
            break
    else:
        sum+=i
        count+=1
print("%d %d"%(count,sum))
