a=[[0],[1,3,1,2,4,5,6],[5,7],[9,11],[11,15,17,3,4,4,5,7],[1,2,3,4]]
i=0
max_len=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[j] < a[i]:
            max_len=a[i]
        else:
            max_len=a[j]
        j=j+1
    i=i+1
print(max_len)

# min=a[0]
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
        
#     if a[i]<min:
