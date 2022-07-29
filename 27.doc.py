# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
print(d)
i=0
while i<len(d):
    j=0
    while j<len(d):
        k=0
        while k<len(d):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])
            k=k+1
        j=j+1
    i=i+1




# for i in range (3):
#     for j in range(3):
#         for k in range(3):
#             print(d[i],d[j],d[k])
