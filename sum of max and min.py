a=[2,3,4,5,6,7,99,100,26,78,79,9]
max=0
min=a[0]
sum=0
i=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    i=i+1
print(max)
print(min)
print(min+max)