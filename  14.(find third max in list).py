a=[29,90,99,201,67,79,10,578,498,433]
i=0
max=0
sec_max=0
third_max=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>max :
             max=a[j]
        if a[j]>sec_max and a[j]!=max:
            sec_max=a[j]
        if a[j]>third_max and a[j]!=sec_max and a[j]!=max:
            third_max=a[j]
        j+=1
    i=i+1  
print(max)      
print(sec_max)
print(third_max)