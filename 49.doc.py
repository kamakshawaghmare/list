#  Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15


a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 's', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="s":
        b=i
    i+=1
print(b)        
