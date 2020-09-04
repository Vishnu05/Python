
# js and python array, list concepts are similar

li = [1, 4, 'string', True, [4, 'hi']]

print('the list are ', li)

print('range of the list starting and ending position ', range(len(li)))
for i in li:
    print(i)

# kind of length, how many times does this loops need to run

for i in range(3):
    print(i)

# concat

car = ['bmw', 'bugati', 'tesla', 'electric car', 'ford']
combine = car + li

print('concat of lists : ', combine)

# slicing them

print(combine[2:])
print(combine[:])

combine.pop()
print('flushed out last element', combine)

# creating list

country = list()
country.append('India')
country.append('England')
country.append('Canada')

# sort function not retruning any values, rather sorted return the list of all values
print('Countries : ', country)
print('Sorting out countries : ', sorted(
    country), 'Length is : ', len(country))

print(country.sort())
no = [8, 3, 0, 9, 1]

print('Sort : ', sorted(no))

tool = ['vs', '++', 'atom']
# print('giving direct value ', tool[2], ' : ', tool['atom'])

# slicing doesn't start with zero, I'm not understanding
t = [9, 41, 12, 3, 74, 15]
print(t[2:4])

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends[0])


# raceback (most recent call last):
#   File "Python\Intermediate\list.py", line 60, in <module>
#     name[0] = 'V'
# TypeError: 'str' object does not support item assignment
name = 'vscode'
# name[0] = 'V'
print('updating the string first char by index : ', name)

# in and not in operator
# print(8 in no)

# large, sum, min

print('Large : ', max(no))
print('Small : ', min(no))
print('Sum : ', sum(no))

# split, if the value is splitted we cannot split it anymore ?

val = 'hello split this string'
val = val.split()

print('Split ', val)

val = 'hello split this string'
val = val.split('s')

print('Split s : ', val)

# sorting the list and reversing the list works fine when we use like this 

# inbulit sort and reverse
food = ['burger', 'pizza', 'icecream', 'nugget', 'corn']
print('Before sorting and reversing ', food)

# sort
food.sort()
print('List has been sorted now ', food)

# reverse
food.reverse()
print('List has been reveresed ', food)


# to check whether the python list is empty or not 

lisst = [1]

# by if else 
if lisst:
    print('List is not Empty')
else:
    print('There is no value in the list')

# by checking the length 
def isListEmpty(lists):
    if len(lisst) != 0:
        return 'Value is there in list'
    else:
        return 'Whoops! nothing in here'

print(isListEmpty(lisst))

# list checking if the value is there are not 

lisst = range(5)

print(len(lisst))