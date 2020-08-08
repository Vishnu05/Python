
# for getting standard input we can use input functions
# by default all the values entered in the input is string have to make explicty typecast to change
# the datatype

a = input('Enter you value : ')

if a.isdigit:
   # print('the input you provided is a number : ' + str(tyep(a)))
   print('hi')
else:
    print('that is a non number')

print('type of input' + str(type(a)))
print('The entered value is ' + str(a))
