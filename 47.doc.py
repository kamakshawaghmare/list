# Write a Python program to convert a given list of strings into list of lists. 
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

a=['Red', 'Maroon', 'Yellow', 'Olive']
c=[]
for i in a:  
    c.append(list(i))
print(c)















# b=[]
# i=0
# while i<len(a):
#     j=0
#     c=[]
#     while j<len(a[i]):
#         c.append(a[i][j])
#         # c.append(k)
#         j=j+1
#     b.append(c)
#     i=i+1
# print(b)