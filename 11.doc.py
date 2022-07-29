# For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 
# and square of 1  is 1.

a=[9,1,1,9]
b=" "
i=0
while i<len(a):
    b=b+str(a[i]**2)
    i=i+1
print(b)


