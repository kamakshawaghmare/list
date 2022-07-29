a=[1,1,2,3,4,4,5,1]
b=[]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    if count>1:
        b.append([count,(a[i])])
    else:
        b.append(a[i])
    i=i+1
print(b)