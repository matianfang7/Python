# 3-1
height=input().split(" ")
sum1=0
for h in height:
    h=int(h)
    sum1+=h
avg=sum1/len(height)
for h in height:
    h=int(h)
    if h>avg:
        print(h,end=" ")
print("")

# 3-2
weight=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
M=('1','0','X','9','8','7','6','5','4','3','2')

n=int(input())
s=list()
allPassed = True
for i in range(n):
    st=input()
    lst=list(st)
    check=[lst[i] for i in range(17) if lst[i]>='0' and lst[i]<='9']
    if(len(check)!=17):#check if there is a character
        allPassed = False
        print(st)
    else:
        count=sum([weight[i]*int(st[i]) for i in range(17)])
        res=count%11
        if(st[17]!=M[res]):
            allPassed = False
            print(st)
if allPassed:
    print("All passed")

# 3-3
s=input()
ch1,ch2=input().split()

lst=list(s)
lst.reverse()
n=len(lst)
for i in range(n):
    if lst[i]==ch1 or lst[i]==ch2:
        print(str(n-i-1)+" "+lst[i])
# 3-20
num = input()[::-1]
isZero = True
count = 0
for i in num:
    if isZero and i=="0":
        count+=1
        continue
    if isZero and i!="0":
        isZero = False
        break
print(str(num[count:]))

# 3-21
s = input()
print(s)
if s == s[::-1] :  
    print("Yes")
else:
    print("No")
