a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     j=0
#     max=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#         j=j+1
#     b.append(max)
#     sum=sum+max
#     i=i+1
# print(b)
# print("sum of max=",sum)





# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]%2==0:
#             # print(a[i][j],"even number")
#             b.append(a[i][j])
#         j=j+1
#     i=i+1 
# print(b)


# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]%2!=0:
#             print(a[i][j])
#             b.append(a[i][j])
#         j=j+1
#     i=i+1
# print(b)

# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i][j]%2==0:
#             print(a[i][j],"even")
#         else:
#             print(a[i][j],"odd")
#         sum=sum+a[i][j]
#         b.append(sum)
#         j=j+1
#     i=i+1
#     print(sum)
# print(b)

a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# max=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i][j]>max:
#             max=a[i]
#             sum=sum+a[i][j]
#         print(sum)
#         j=j+1
#     i=i+1
# print(max)

# a=[
    
i=1
while i<=7:
    j=1
    while j<=i:
        if j%2!=0:
            print(j,end=" ")
        else:
            print("*",end=" ")
        j=j+1
    print( )
    i=i+2


    



