i=1
while i<=7:
    j=1
    while j<=i:
        if j%2!=0:
            print(j,end='')
        else:
            print("*",end=" ")
        j=j+1
    print()
    i=i+1

1
1*3
1*3*5
1*3*5*7