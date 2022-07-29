a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
i=0
l=[]
while i<len(a):
    if a[i] not in b:
        l.append(a[i])
    i+=1
print(l)        

