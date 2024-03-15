 str=input()
LL=[]
UL=[]
numbers=[]
operators=[]
special_symbols=[]
for i in str:
    for j in range(97,122):
        if i==chr(j):
            if i not in LL:
                LL.append(i)
    for j in range(65,90):
        if i==chr(j):
            if i not in UL:
                UL.append(i)
    if ord(i)>=48 and ord(i)<=57:
            if i not in numbers:
                numbers.append(i)
    if  i=='+'or i=='-' or i=='*' or i=='/':
        if i not in operators:
            operators.append(i)
    elif(ord(i)>=1 and ord(i)<=47) or(ord(i)>=58 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=127):
        special_symbols.append(i)
print(LL)
print(UL)
print(numbers)
print(operators)
print(special_symbols)
