n=int(input())
a=[]
even=[]
odd=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("The even list",end=' ')
print(even)
print("The odd list",end=' ')
print(odd)
