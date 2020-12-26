
# I Have noticed that you dont have to declare the type just give the values and use it
# it is cool but, while debugging can cause issues 

name = 'vishnu'
print(name)

print(type(name))

a = 10
b = 234

print (a + b)
print(type(a))

boolean = True
print(type(boolean))

array = [1, 3, 5, 6, 6, 9, 10]
print(array)
print(type(array))

print('Into the arrays ')

arrayLength = list.__sizeof__(array)

for arrayLength in array:
    print(array)
    #print(array[a])
   # print(array)

# string has more methods, like evaluating and doing other stuff around
country = 'india'

# type casting needs to be done when concatenation
print('length of the country : ' + str(country.__len__()))


# copying the variable vs assigning to them
# this is working fine, but for the list it is different, values are assigned as same reference 

lap = 'windows 10'
hp = lap

print('Value of string varible ', lap, hp)

hp = 'windows 10 home edition'

print('After changing the value ', lap, hp)

# dict? 

book = dict()


book[2] = 'hi'
print('dictionary ', book)

val = book

val[2] = 'value'
print(val)
