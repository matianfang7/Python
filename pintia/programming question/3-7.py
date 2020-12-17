n=int(input())
lst=list(map(int,input().split()))
maxnum = max(lst)
print(str(maxnum)+" "+str(lst.index(maxnum)))
