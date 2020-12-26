print('hello world')


# operator precedence
x = 1 + 5 * 10 / 2 - 4

# normal way answer will be 26, with operator precedence 21
# mulitplication, division (quotient), addition and subtraction
#  5 * 10 = 50, 50 / 2 = 25, 25 + 1 = 26, 26 - 1 = 22

print(x)

# normal way of execution but we have to tell the program how to execute it
x = ((((1 + 5) * 10) / 2) - 4) 

print('1' + 'i')

# interesting part have to learn about the rounding concepts
print(int(98.9))
print('using round method ' + str(round(98.9)) + ' : ' + str(round(98.4)))

print(x)

# to be honest this typecasting is sucks, what ever the input we are typing it is string
# then it is need to be explictly convert into corresponding data type

hours = input('enter hours : ')
hours = int(hours)
print(type(hours))

rate = (2.75)
pay =  (hours * rate)
print(type(pay))
print(pay)

