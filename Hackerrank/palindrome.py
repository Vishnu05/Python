

val = input('Enter the value to check : ')
s = val

check = list()
result = list()

for i in s:
    check.append(i)
    result.append(i)

result.reverse()

if (check == result):
    print('yes')
else:
    print('no')
