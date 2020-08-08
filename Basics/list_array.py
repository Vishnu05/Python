
# in python list are array

a = [1, 1, 1, 1, 1, 3, 5, 6, 7, 8, 10, 23, 'hi', True, 2.35]
print(a)
print(type(a))

b = [4, 564, 34, 66, 934]

# appending will add a element in the end of the list
a.append('Adding a string')
print(b.sort)

a.reverse()

# insert will add a element begining of the list, (index, object)
a.insert(1, 1110)
print(a)

# to count a specific element occurence 
print(a.count(1))

# 1 is the value need to be checked under a, and a should be an iterable one
if 1 in a:
    print('true')
else:
    print('false')

string = ['strings', 'name', 'age', 'gender']
if 'name' in string:
    print('String is present ' + str(string))
else:
    print('string is not present')