
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
# appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

# more optimized soultion can be coded, needs improvement

fileName = input('Enter the fileName : ')
fileHandle = open(fileName)

val = ''
dic = dict()
lists = list()
for i in fileHandle:
    if not i.find('From '):
        val = val.__add__(i)
        # iterating the file each line by line and adding to the list
        lists.append(i)
        # val = val.split()
        # dic[val[1]] = dic.get(val[1], 0) + 1

value = ''
splitVal = ''
for i in lists:

    # storing the values in the string and splitting up to get email address
    value = i
    splitVal = value.split()

    # adding in the dictionaries and at the same time counting the values
    dic[splitVal[1]] = dic.get(splitVal[1], 0) + 1
    # print('values are ', splitVal[1])

maxValue = 0
high = ''

# checking highest value in the dictionaries
for i in dic:
    if maxValue < dic[i]:

        # value
        maxValue = dic[i]
        # key
        high = i

print(high, maxValue)

a = [1, 6, 9, 0, 83]
for i in a:
    if maxValue < i:
        maxValue = i


print('Max value is : ', maxValue)

# for i in dic:

keyMax = max(dic, key=dic.get)
print('keymax value : ', keyMax, dic[keyMax])

# print(max(dic), dic[max(dic)])
# print('dict values are : ', dic)

# writing into the file
write = open('email.txt', 'w')
write.write(val)

# print('Value is : ', val, lists)
