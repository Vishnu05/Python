# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' 
# like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of 
# the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# optimized code can be improved, intial version for now 

fileName = input('Enter the file name : ')
fileHandle = open(fileName)

# this code should be done via lists, but done with simple string

# lists = []
count = 0
val = ''
# newList = []

# iterating through each line 
for i in fileHandle:
    # I'm not sure about the not function, if it finds the word starts with from, then procceed further 
    if not i.find('From: '):

        # adding in list no use of this 
        #lists.append(i)

        # adding the vales as string 
        val = i

        # splitting up and hardcoding the index for getting email values  
        val = val.split()
        print(val[1])
        count = count + 1
        
# print('value : ', lists)
# print('Total values are : ', count)
print("There were", count, "lines in the file with From: as the first word")

