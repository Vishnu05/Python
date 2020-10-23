
# list comprehension

planet = []
print('type of planet', type(planet))

# normal for loop approach 
for i in 'earth sun moon':
    planet.append(i)

print('After adding elements in list', planet)

# using list comprehension approach 
# syntax - [expression for item in list]
planet = [i for i in 'Earth']
print('using list comprehension', planet)

# using lambdas 

ins = []

ins.insert(2, 8)
ins.insert(5, 10)
ins.insert(0, 'hello')
print(ins)

# nested list, Making a nested list 

main = list()

# how many times does this loop needs to be executed 
n = int(input('Enter the value of n : '))

# how much values should nested loop needs to hold as of now
m = int(input('Value for nested loop : '))

for i in range(n):
    sec = list()
    for i in range(m):
        sec.append(input())
    main.append(sec)

print('Nested loops ', main)

    

