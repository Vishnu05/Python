
# if else 

# programm for voting 18+ can vote in india

age = input('Enter your age: ')
age = int(age)

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
