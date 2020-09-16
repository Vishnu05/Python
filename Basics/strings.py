
# Strings

name = 'vishnu'
print(name[2])

for i in name:
    print(i)

print('length of the string : ', len(name))

name = 'Hi this is length Im going to check'
print('values : ', len(name), ' _len_ ', name.__len__())

# split and slice method
# split, if we give a character in a lengthy string it will break them out and print them
# splice is like it will cut or get a particular portion of he string

print('split method : ', name.split('o', 4))
print('slice method full : ', name[2:8])
print('slice method right :', name[:2])
print('slice method left :', name[2:])
print('slice method  none :', name[:])


for i in name.split('i',  1):
    print('Split : ', i)


# in operator also check the strings

print('python in operator : ', 'i ' in name,
      '  :  ',  'if doesnt exits : ', 'z' in name)

# string comparions 

if 'a' > 'A':
    print('Captial ')

print('upper case : ', name.upper())

# retruns the position of the string in array format, character wise 
print('find in a string : ' , name.find('hi'))


a = '40' 

b = int(a) + 2
print(b)

x = 'From marquard@uct.ac.za'
print(x[15:18])

print(len('hi')*3)

# trimming white space 

a = '    this contains white space          '
print(a.strip())

a = 'hello'
b = a.find('e')
print(a[0:1])
print(a[b:b+2])


# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

# reverse a string 

word = 'abcdef'

reverse_word = word[::-1]
print('reversed word is ', reverse_word)

# list to strings