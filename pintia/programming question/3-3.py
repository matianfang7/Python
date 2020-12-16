s=input()
ch1,ch2=input().split()

lst=list(s)
lst.reverse()
n=len(lst)
for i in range(n):
    if lst[i]==ch1 or lst[i]==ch2:
        print(str(n-i-1)+" "+lst[i])

