# List product excluding duplicates.
    # List = [6,1,3,5,6,3,1]
    # Output: 60

a=[6,1,3,5,6,3,1]
i=0
product=1
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        product=product*(a[i])
    i=i+1
print(product)


