n=int(input())
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)
