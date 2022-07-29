a=[15,17,19,22,45,65,2]
count=0
b=len(a)
i=0
while i<b:
    if a[i]%2!=0:
        count=count+1
    i=i+1
print(count)