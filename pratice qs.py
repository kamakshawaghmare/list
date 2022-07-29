# a=[-1,2,-3,-9,5,7,3,8,9,-1]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(1)
#     else:
#         b.append(0)
#     i=i+1
# print(b)

a=[-1,2,3,-4,5,-6,-7,-8,0]
b=[]
i=0
while i<len(a):
    if a[i]>=1:
        b.append(1)
    else:
        b.append(0)
    i=i+1
print(b)