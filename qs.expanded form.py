# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'

a=input("enter the number:")
b=[]
i=0
while i<len(a):
    k=len(a)-(i+1)
    if a[i]=="0":
        print(end="")
    else:
        s=int(a[i])*(10**k)
        # b.append(s)
        print(s,end="+")
    i=i+1