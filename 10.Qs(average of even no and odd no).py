a=[23,14,56,12,19,9,15,25,31,42,43]
avg=0
i=0
count=0
while i<len(a):
    if i%2==0:
        count=count+i
    i=i+1
print(count)
avr=count/len(a)
print(avr)