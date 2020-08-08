# conditions and loops

a = 5
b = 10

if a < b:
    print("it is greater")
else:
    print("it is lesser ")

name = "vishnu"
name = False

if type(name) == str:
    print("String")
else:
    print("not a string")

# in python there is no array i guess, it is there but in the name of list

names = [
    "c",
    "c++",
    "I like java",
    "Javascript is cool",
    "ruby I have no idea",
    "kotlin for android",
]

len = list.__sizeof__(names)

for len in names:
    # it gives the full list of array elements
    # print(names)

    # where len gives each and every element
    print(len)
    # print(names.count)

# division of 2
div2 = [2, 4, 6, 8, 10]
len = list.__sizeof__(div2)

for len in div2:
    print(len / 2)
    print(2 * len)


# for a in b:
#     print("hello python loop")

while div2.__sizeof__() > 3:
    print("while loop i have no idea haha")
    break
a = 5
# while a < 6:
#     print('print these 5 times')

# for a in a:
#     print('run for ')


companies = ['google', 'amazon', 'facebook', 'microsoft', 'netflix', 'uber']

# why python all the values need to be explictly string when concatenations ?

print('The companies are : ' + " " + str(companies) + " : " + companies[3])

# i is the iterator element and companines is list(array) where it has to be an array or object element
for ii in companies:
    print(ii)
    # print('%s %d' %(ii, d[ii]))


print(vars)