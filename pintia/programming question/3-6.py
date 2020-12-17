lst,times= list(input().split())[1:],0
for i in lst:
    t = lst.count(i)
    if t>times:
        times=t
        who=i
print(who,times)

