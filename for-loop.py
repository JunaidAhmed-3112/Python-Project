z=[6,4,8]
target=4
for i in range(0,len(z)):
    for j in range(i+1,len(z)):
       list=z[i]-z[j]
       list1=abs(list)
       print(list1)

