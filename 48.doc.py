# WriWrite a Python program to split a given list into specified sized chunks. 
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]


a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83,]
i=0
b=[]
# c=3
while i<=len(a)-3:
    b.append(a[i:i+3])
    i=i+3
print(b)




