inp=input().split()
res=""
for i in inp:
    if(len(i)>len(res)):
        res=i
print(res,len(res))