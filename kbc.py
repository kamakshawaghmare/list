# print("let start KBC")
# print("it is your question")
# q=["q.1 who is the prime minister of the indea 2020 ?",
# "who is the father of the nation",
# "who is the father of indian contitution"]

# a=int(input("enter the num"))
# i=1
# while i<a:
#     name=input("enter the name")
#     print(name)
#     i=i+1

i=1
while i<8:
    j=1
    while j<i:
        # print(j,end=" ")
        if j==2 or j==4:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    i=i+1

