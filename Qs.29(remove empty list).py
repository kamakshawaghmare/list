# Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]


a=[5,6,[],3,[],[],9,[],2,3,4,[],[]]
# list.remove([]),list.remove([]),list.remove([])
# list.remove([])
# print(list)

i=0
b=[]
while i<len(a):
        if a[i]==[] :
            print(a[i])
        else :
            b.append(a[i])    
        i=i+1
print(b)