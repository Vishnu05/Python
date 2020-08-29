

files = open('pyw.txt', 'w')
filesr = open('py.txt', 'r')

print(files)

val = files
print(val)

files.write(' New line in the text file')
files.write('blah blah blah ')

# this is how files can be readed
count = 0
for i in filesr:
    print(i)
    count = count + 1


print('file lenght is : ', count)


# rstip
print('hello start ')
for i in filesr:
  #  i = i.rstip()
    print('printing : ', i)

print('hello ends ')

# storing the data in string 

fileName = open('pyw.txt')
valStr = filesr.read()

print('Value is readed as string : ', valStr)

# user types the file name

while True:
    fileName = input('Enter the file name you want to open : ')

    try:
        fileToOpen = open(fileName)

        for i in fileToOpen:
            print(i)
        print('Happy to inform you that you have viewed the file')
        break
    except Exception as e:
        print('you have entered a file that doesnt even exits for your kind information ')
        print('error is : ', e)
        quit()

