list1=[24, -5, 0, 99, -12, 24, 7]
# list1.sort()
# print(list1)

for i in range(len(list1)):
    for j in range(0,len(list1)-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp

print(list1)            