# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split()
#  method. The program should build a list of words. For each word on each line check to see if the word is already in the
# list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical
# order. You can download the sample data at http://www.py4e.com/code3/romeo.txt


# not sure if this soultion is an optimized one or not but works fine for now

fileName = input('Enter the file name : ')
fileHandle = open(fileName)

# empty lists and string
lists = []
val = ''

# concating the whole string file into a single string value
for i in fileHandle:
    val = val + i

# adding it to list and splitting each word by space
for i in val.split():
    lists.append(i)

# sorting it out
sort = sorted(lists)

# creating a new list, checking if the list contain the value or not
newList = []
for i in sort:
    if not newList.__contains__(i):
        newList.append(i)

print(newList)


# sorting it out
# newList = sorted(lists)
#comma = newList.split(',')

# string split

print('Lists : ', newList)
