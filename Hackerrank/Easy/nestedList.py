
n = int(input("input : "))

lists = list()
for i in range(n):
    nested = list()
    nested.append(input())
    nested.append(float(input()))
    lists.append(nested)

lists.sort()
print('Nested array : ', lists)

for i in lists: 
    print('value of the Keys : ', i[0] )