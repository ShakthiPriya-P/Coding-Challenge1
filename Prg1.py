inp=input().strip()
for i in range(1,len(inp)):
    if(inp[i].isdigit()):
        if(inp[i-1].isalpha()):
            dig=inp[i]
            char=inp[i-1]
        elif(inp[i-1].isdigit()):
            dig+=inp[i]
    if(inp[i].isalpha() or i==len(inp)-1):
        print(char*int(dig),end='')