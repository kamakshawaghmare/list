# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


a=[['g','f','g'],['i','s'],['b','e','s','t']]
sum=""
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+(a[i][j])
        j=j+1
    i=i+1
print(sum)

