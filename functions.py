'''
def multiplication_numbers (a,b):
    multiplication=(a*b)
    return multiplication
result=multiplication_numbers(5,5)
print(result)
'''
'''
a=[2,7,6,4,1]
for i in range(len(a)):
    if a[i]%2==0:
       print(a[i])
'''
"""
def even_numbers(a):
a=[2,7,6,4,1]
for i in range(len(a)):
    if a[i]%2==0:
       print(a[i])
result=even_numbers(a)
print(result)
"""
"""
a = [28, 92, 33, 45]
b=35
z=[]
for i in range(len(a)):
    if a[i]>b:
        z.append(a[i])
print(z)
"""
""""
z=[]
def greater_number(a,b):
    for i in range(len(a)):
        if a[i] > b:
            z.append(a[i])
    return z
a = [28, 92, 33, 45]
b=35
result=greater_number(a,b)
print(result)
"""
"""
#
list1 = [1,2,4]
list2 = [1,3,4]
list3 = list1 + list2
list3.sort()
print(list3)
def sorting(list1, list2):
    list3 = list1 + list2
    list3.sort()
    print(list3)

list1 = [1, 2, 4]
list2 = [1, 3, 4]
sorting(list1, list2)

list51= [2,3,5]
list52 = [3,5,6]
sorting(list51,list52)
"""
nums=[1,1,2,3,2,5,6,6]
new= list(set(nums))
k = len(new)
print(new,k)

