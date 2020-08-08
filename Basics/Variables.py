
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
