maps = dict()

maps[3] = 'Name'
maps['strings'] = 23
maps[True] = False
print(maps, type(maps))

val = {3: 'Name', 'strings': 23, True: False}

print(maps, type(maps))

# hashmap or hashtable in java
# dictionaries are in python

val = ['max', 'glen', 'alex', 'robert', 'jr', 'alex',
       'robert', 'jr', 'max', 'glen', 'alex', 'robert', 'jr']

# couting the words

count = 0
dic = dict()

# dictionaries doesn't allow duplicate keys

for i in val:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1

print('Initial dic value : ', dic)


# simplified version of counting with built in get method
dic.clear()
# print(dic)

for values in val:
    # value is key and, 0 is inital value for that key
    dic[values] = dic.get(values, 0) + 1

print('Dic values are : ', dic)

# for i in dic:
#     print('dictionaries in for loop : ', dic.get(i))

# keys method reterive only the keys of dict

intoTheList = list(dic)

print('Lists are : ', intoTheList)
print('reterive only the keys : ', dic.keys())
print('Reteriving the values : ', dic.values())

# tuples ?? 
print('Tuples : ', dic.items())


# cool stuff two iteration variable 

for key, values in dic.items():
    print(key, values)


print(dic.get('names', 3))

# using input inserting values in dictionary 

# val = dict()

# print('Inserting values in dictionary using input ')

# n = int(input('Enter the value range : '))

# for i in range(n):
#     li = list()
#     val[input()] = li
#     print('before the list')
#     for i in range(3):
#         li.append(input())
#     print('after the list')
    
# print('dictionary values are ', val)

    
# reterive the values, using key 

val = dict()

val['one'] = [1 , 3]
val['two'] = [3, 4]

a = input('Enter the value to find out')

v = val.get(a)

print('value of dict ', val, 'getting the value using key' , v )


