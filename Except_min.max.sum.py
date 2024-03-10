lst=list(map(int,input().split()))
lst.sort()
sum=0
for i in lst:
      if i== lst[0] or i==lst[-1]:
       lst.remove(i)
for i in lst:
    sum=sum+i
print(sum)
