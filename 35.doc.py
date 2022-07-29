# Write a Python program to check if first digit/character of each element in a given list is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if the first digit in each element of the given list is the same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False


l=[1234, 122, 1984, 19372, 100]
b=str(l[0])[0]
i=0
count=0
while i<len(l):
    a=str(l[i])
    if a[0]==b:
        count=count+1
    i=i+1
if count==len(l):
    print("true")
else:
    print("false")



# code for abc printing

# a=['aab', 'abc', 'ab', 'ha', 'ac']      
# i=0
# while i<len(a):
#     # print(a[i][0])
#     if a[i][0]=="a":
#         print("true")
#     else:
#         print("false")
#     i=i+1