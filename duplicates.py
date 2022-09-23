n=int(input())
a=[]
b=[[]]
for i in range(0,n):
    t=int(input())
    a.append(t)
for i in a:
    if i not in b:
        b.append(i)
print(b)
