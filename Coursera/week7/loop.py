


largest = -1
lis = []

while(True):
    value = input('Enter the value ')
    try:
        if value == 'done':
            break
        value = int(value)
        if value > largest:
            largest = value
        lis.append(value)
    except:
        print('Invalid input')

smallest = min(lis)
print('Maximum is ', largest)
print('Minimum is ', smallest)
