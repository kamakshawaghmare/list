a=[2,4,5,6,7,8,9]
b=len(a)
avr=0
sum=0
i=0
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
    i=i+1
avr=sum/b
print(avr)
