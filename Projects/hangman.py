
# basic hangman game,

# word character less than 5 for now, each letter, each chances
# List, in python if a list is copied it actually never copies the entire list value rather it copy the refereence
# of the list. When ever the list changes the refferenced value of list of changes 

import random

print('welcome to Python hangman game!')

category = ['Movies', 'Sports', 'City']

# using random selecting what kind of category want to play
catValue = random.randrange(0, 3)

# print('catvalue is ', catValue)
print('The choosen Category is :', category[catValue])
print('You have roughly 5 chances to find out the Clue')

subCategory = [['batman', 'inception', 'rush',
                'forrestgump', 'thor'],
               ['football', 'basketball', 'longjump', 'shotput', 'formula1'],
               ['new-york', 'chennai', 'stockholm', 'amsterdam', 'london']]

hints = [['The man who does good thing to people, Billionare!!', 'Stealing the dream', 'James Hunt and Nikki lauda',
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

# Assigning the hangman word to variable value
value = s[subValue]
# print('Value of s ', value)

print('Length of the Character is ', len(value))

life = 5

valueList = list()
for i in value:
    valueList.append(i)

# print('value in list ', valueList)

# count = 5
answer = list()

# making all the values empty, when ever user gives the correct input values is updated
for i in valueList:
    answer.append('')

# print('Answer is : ', answer)

select = list()

for i in valueList:
    select.append(i)

# print('select value is ', select)

# this is only for iteration purpose later, it needs to be refactored
dummy = valueList

finalAnswer = ''

# chaning from for loop to while loop is more control for me
while life > 0:
    val = input('Enter your guess : ')

    # if condition to make sure the entered value is present in list
    if val in valueList:
       # life = life + 1

        for j in dummy:
            index = 0
            if val in j:
                index = valueList.index(val)
                answer[index] = valueList[index]
                dummy[index] = ''
        print('So far you have found : ', answer)

    else:
        print('You have entered a value that doesnt belong to hangman search')
        life -= 1

    # print('the valueList and answer : ' , select == answer, 'original value is : ', select, ' guessed one : ', answer)
    if answer == select:
        print('Hoorahyy... You have gessed the word... Congrats',
              'the word is', "==>", finalAnswer.join(answer))
        break

    print('You have more ', life, 'chances ')


if (life <= 0):
    print('The word is ', value)
    print('All the chances have been exhausted, Start again ')
# print ('value list and answer checking whether both are same or not', valueList == answer, 'original : ', valueList, 'answered : ', answer)

# print(s)
# print(h)
# print('the value is :', s[subValue])
# print('The hint is :', h[subValue])
