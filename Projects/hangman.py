
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

count = 10
answer = list()

for i in range(10):
    val = input('Enter your guess: ')
    try:
        index = valueList.index(val)
        if val == valueList[index]:
            answer.insert(index, valueList[index])
    except:
        print('You have entered a character that doesnt belong to the game')
   
    print("Your guess is : ", answer)



# print(s)
# print(h)
# print('the value is :', s[subValue])
# print('The hint is :', h[subValue])
