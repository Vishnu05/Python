
# basic hangman game,

# word character less than 5 for now, each letter, each chances

import random

print('welcome to Python hangman game!')

category = ['Movies', 'Sports', 'City']

# using random selecting what kind of category want to play
catValue = random.randrange(0, 3)

print('catvalue is ', catValue)
print('The choosen Category is :', category[catValue])
print('You have roughly 10 chances to find out the Clue')

subCategory = [['batman', 'inception', 'rush',
                'forrest-gump', 'thor'],
               ['football', 'basketball', 'longjump', 'shotput', 'formula-1'],
               ['new-york', 'chennia', 'stockholm', 'amsterdam', 'london']]

hints = [['The man who does good thing to people', 'Stealing the dream', 'James Hunt and Nikki lauda',
          'the guy runs entire US', 'Super hero who has hammer'],
         ['All around the world people love this game', 'In america one of the best games people watch',
             'It is all about the jump', 'Throwing heavy object for long distance', 'best race ever in world'],
         ['The city never sleeps', 'World second largest beach', 'Abba museum.', 'Second famous cananls country',
          'Royal Families']]

s = subCategory[catValue]
h = hints[catValue]

subValue = random.randrange(0, 5)

print('Hint is !!!: ---> ', h[subValue])
# print('subvlalue is ', subValue)

value = s[subValue]
# print('Value of s ', value)

print('Length of the word is ', len(value))

life = 10

valueList = list()
for i in value:
    valueList.append(i)

print('value in list ', valueList)

dummy = valueList

print('dummy is ', dummy)

count = 10
answer = range(len(value))

for i in range(10):
    val = input('Enter your guess: ')
    countInside = 0

    # iterating through list 
    index = 0
    for j in valueList:
        if valueList:
            index = valueList.index(val)
            print('value of the index is : ', index, ' entered the value ', val)
            if val == dummy[index]:

                # if value is found poped out of the list 
                dummy.pop(index)

                # getting the index
                ind = dummy.index(j)

                # Anding into the list 
                answer.insert(ind,j)
                index = index + 1
    print("Your guess is : ", answer)



# print(s)
# print(h)
# print('the value is :', s[subValue])
# print('The hint is :', h[subValue])
