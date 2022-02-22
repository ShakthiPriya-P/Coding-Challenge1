inp=input().strip()
char=inp[0]
count=1
for i in range(1,len(inp)):
    if(inp[i]==char):
        count+=1
    elif(inp[i]!=char):
        print(inp[i-1]+str(count),end='')
        char=inp[i]
        count=1
    if(i==len(inp)-1):
        print(inp[i]+str(count))