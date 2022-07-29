#  Write a Python program to iterate a given list cyclically on specific index position. 
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
s=[]
sp=int(input("enter the specific index:"))
while i<1:
    b=a[sp:]+a[0:sp]
    s.append(b)
    i=i+1
print(s)
    