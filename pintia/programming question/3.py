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

# 3-4
ch=input()
string=input()
n=string.rfind(ch)
if n!=-1:
    print("index = "+str(n))
else:
    print("Not Found")

# 3-5
s=input()
n=""
for i in range(len(s)):
    if "0"<=s[i]<="9":
        n+=s[i]
print(int(n))

# 3-6
lst,times= list(input().split())[1:],0
for i in lst:
    t = lst.count(i)
    if t>times:
        times=t
        who=i
print(who,times)



# 3-7
n=int(input())
lst=list(map(int,input().split()))
maxnum = max(lst)
print(str(maxnum)+" "+str(lst.index(maxnum)))

# 3-8
n=input()
#print(n[::-1])
#print(str((list(n).reverse())).join(""))
n=list(n)
n.reverse()
str=""
print(str.join(n))

# 3-9
dic,s='0123456789abcdefABCDEF',''
st=input()
for i in st:
    if i in dic:
        s+=i
    if i=='#':
        break
if s=='':
    print(0)
else:
    num=int(s,16)
    if st.find('-')<st.find(s[0]):
        num=-num
    print(num)

# 3-10
Str = input()
count=0
for i in Str:
    if "A"<=i<="Z":
        if i!="A" and i!="E" and i!="I" and i!="O" and i!="U":
            count+=1
print(count)

# 3-11
lst = input().split()
lst.sort()
print("After sorted:")
for i in lst:
    print(i)

# 3-12
n = list(input())
result = sum([int(i) for i in n])
print(str(len(n))+" "+str(result))

# 3-13
Str = input()
result = ""
for i in Str:
    if "A"<=i<="Z":
        result+=chr(ord('Z')-ord(i)+ord("A"))
    else:
        result+=i
print(result)

# 3-14
Str = input()
result = ""
for i in Str:
    if i == "#":
        break
    if i.isalpha():
        if "a"<=i<="z":
            result+=i.upper()
        else:
            result+=i.lower()
    else :
        result+=i
print(result)

# 3-15
# 1.输入
s=input()

# 2.处理
words=s.split()
        
# 3.输出
print(len(words))

# 3-16
Str = list(input())
Str.sort()
result = ""
pre = ""
for i in Str:
    if i !=pre:
        pre = i
        result+=i
print(result)

# 3-17
Str = input().strip()
ch = input().strip()
Str=Str.replace(ch.lower(),"").replace(ch.upper(),"")
print("result: "+str(Str))        
        
# 3-18
Str = input()
result = ""
count = 0
for i in Str:
    if i.isalpha() and i.lower() not in result and i.upper() not in result :
        result+=i
        count+=1
    if count==10:
        break
if count==10:
    print(result)
else:
    print("not found")

# 3-19
n = int(input())
maxStr = ""
for i in range(n):
    Str=input()
    if len(Str)>len(maxStr):
        maxStr=Str
print("The longest is: "+maxStr)

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
