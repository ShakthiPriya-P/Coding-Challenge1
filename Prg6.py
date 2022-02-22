inp=int(input())
fact=1
for i in range(1,inp+1):
    fact*=i
ct=0
while(fact%10==0):
    ct+=1
    fact//=10
print(ct)