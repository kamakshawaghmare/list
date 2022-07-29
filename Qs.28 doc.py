# he task is to perform the operation of removing all the occurrences of a given item/element present in a list.
# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2

a=[1,1,2,3,4,5,1,2]
# i=0
# b=[]
# while i<len(a):
#     if b not in a[i]:
#         print(a)
#     i=i+1
# print(set(a))
a.remove(1),a.remove(1),a.remove(1)
print(a)
