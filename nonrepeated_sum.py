st1=map(int,input().split())
lst2=[]
sum=0
for i in lst1:
    if i not in lst2:
        lst2=lst2+i
    else:
        lst.remove(i)
for i in lst2:
    sum=sum+i
print(sum)
