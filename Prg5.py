n=int(input())
list1=[]
for i in range(n):
    list2=[]
    for j in range(i+1):
        if(j==0 or j==i):
            list2.append(1)
        else:
            list2.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(list2)
for i in range(n):
    print(" "*(n-i-1),end='')
    print(*list1[i])