n1=int(input())
a=[]
c=[]
b=[]
for i in range(0,n1):
    t=int(input())
    a.append(t)
n2=int(input())
for i in range(0,n2):
    z=int(input())
    b.append(z)
c=a+b
print("Sorted list is:",end=' ')
print(sorted(c))
