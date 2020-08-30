
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the 
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fileName = input('Enter the file name: ')
fileHandle = open(fileName)

lists = list()
for i in fileHandle:
    if not i.find('From '):
        lists.append(i)

# write = open('time.txt', 'w')
val = ''
splitVal = ''
dic = dict()
for i in lists:
    val = i
    val = val.split()
    splitVal = val[5]
    #write.write(val[5], '\n')
    splitVal = splitVal.split(':')
   # print('Hour split : ', splitVal[0])
    strr = str(splitVal[0])

    dic[strr] = dic.get(strr, 0) + 1

dicList = sorted(dic)

for i in dicList:
    print(i, dic[i])
