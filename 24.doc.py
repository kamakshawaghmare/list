# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

list=[1,2,3,1,2,2]
b=[]
i=0
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)