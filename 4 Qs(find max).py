list=[10,50,126,67,89,99,100,2,23,]
# print("maximum of list is =",max(list))

i=0
max=0
max1=0
while i<len(list):
    if list[i]>max:
        max=list[i]    
    i+=1
print(max)