
# if else 

# programm for voting 18+ can vote in india

# age = input('Enter your age: ')
# age = int(age)
age = 1

if age < 18:
    print('You are not eligible for voting....')
else:
    print('Your vote, your choice to ellect the people ')

if age > 0:
    if age < 18:
        print('Nope')
    elif age > 110:
        print('invalid data : try between 1 - 109')
    else:
        print('Choose your vote wisely')
else:
    print('wrong input')


# break and continue statement

for val in '112112112':
    if val == '2':
        print('value has been founded : ' + str(val))
        print('break statement')
        # break
        continue
    print(val)
print(val.__len__)
print('after for')


# tabs and spaces 

if 5 > 4:
    print('hello')
if 7 > 3:
     print('')