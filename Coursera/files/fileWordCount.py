# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking
#  for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of
# those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter
# mbox-short.txt as the file name.


fileName = input('Enter the file name : ')
fileHandle = open(fileName)

count = 0
lineCount = 0
for i in fileHandle:

    if not i.find('X-DSPAM-Confidence: '):
        val = i

        finds = val.find(':') + 1
        # print('values are ', val, ' find ', finds, ' type of val ', type(val))
        # print(i[finds:])
        count = count + float(i[finds:])
        lineCount = lineCount + 1

avg = count / lineCount

print('Average spam confidence : ', avg)
