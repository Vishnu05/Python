
# dictinory coding

import math

val = dict()

n = int(input())

for i in range(n):
    names = input().split()
    li = list()
    val[names[0]] = li
    # print('before making the list')
    count = 1
    for i in range(3):
        li.append(names[count])
        count += 1
    # print('after the list')

# print('dictionary value ', val)

# to get the average details of the student
name = input()

ave = val.get(name)

# print('average student name is ', ave)

count = 0
for i in ave:
    count += float(i)

ans = (count/ len(ave))


print('{0:.2f}'.format(ans))
