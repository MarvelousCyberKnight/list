n=int(input())
a=[]
mean=0
for i in range(0,n):
    t=int(input())
    a.append(t)
for i in a:
    mean=mean+i
average=mean/n
print("%.1f"%average)
