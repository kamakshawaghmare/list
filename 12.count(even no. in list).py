a=[12,45,66,22,78,90,78,22,6,8]
sum=0
i=0
b=len(a)
while i<b:
    if a[i]%2==0:
        sum=sum+1
    i=i+1
print(sum)