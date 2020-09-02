

# set datastructure allows only unique values and it doesn't contian duplicate values

val = set()

val.add(34)
val.add(10)
val.add('dsdf')
print(val)

n = int(input('Enter how many values to be added in set : '))

for i in range(n):
    val.add(input())

print('Set vales are : ' , val)

for i in val:
    print('Iterating the sets : ', i)

print('size of the set ', val.__sizeof__(), ' length of the set ', len(val))