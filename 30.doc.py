# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

# list=[2,-7,5,-64,-14,8,3,4,5,6,7,8,1,0]
# b=[]
# positive_c=0
# negative_c=0
# i=0
# while i<len(list):
#     if list[i]>0:
#         positive_c=positive_c+1

#     else:
#         negative_c=negative_c+1
#     i=i+1
# print(positive_c)
# b.append(positive_c)
# print(negative_c)


list=[2,-7,5,-64,-14,8,3,4,5,6,7,8,1,0]
b=[]
c=[]
n_count=0
p_count=0
i=0
while i<len(list):
    if list[i]>0:
        p_count=p_count+1
        b.append(list[i])
    else:
        n_count=n_count+1
        c.append(list[i])
    i=i+1
print(b,p_count)
print(c,n_count)