n=int(input())
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
a.remove(max(a))
d=max(a)
print(d)
