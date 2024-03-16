str1=input()
str2=input()
lst1=[]
lst2=[]
Flag=True
for i in str1:
     lst1.append(i)
for i in str2:
    lst2.append(i)
for i in lst1:
     if i not in lst2:
       Flag=False
if(Flag==True):
      print("anagram")
else:
    print("not anagram")
