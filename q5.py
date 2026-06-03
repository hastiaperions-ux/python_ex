a=int(input("enter a num :"))
b=int(input("enter a num :"))
c=int(input("enter a num :"))
d=int(input("enter a num :"))


max=a
if b>a and b>c and b>d:
    max=b
elif c>a and c>b and c>d:
    max=c
elif d>a and d>b and d>c:
    max=d
print(max)

