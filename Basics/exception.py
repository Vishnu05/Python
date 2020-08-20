
a = input('enter the value : ')

# if the input is integer there is nothing needs to be done, other than that
# errors gonna throw in this scipt
# basics of exception handling
# traceback

try:
    a = int(a)
# except Exception as i:
    # print(i.args)
    # print(i)
    # print(' i guess it is a catch block ')
finally:
    print('whatever happens I"m going to run because that is what I intended for')

# assigning the value in catch, except block

b = input('Enter the wrong data : ')

try:
    b = int(b)
except:
    b = 10

print('The value of b is : ', b, ' : ', a)

no = 40 * 10.5

c = 5 * (10.50 * 1.5)
ans = no + c
print(ans)

