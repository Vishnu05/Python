

a = input('Enter the input : ')

li = a.split(' ')
print('input is : ', li)

# basic apprach, navie solution

n = int(input())

list = list()
for i in range(n):
    val = input()
    li = val.split(' ')

    # planning to replace if statement with in a different way 
    if li[0] == 'insert':
        list.insert(int(li[1]), int(li[2]))
    if li[0] == 'print':
        print(list)
    if li[0] == 'remove':
        list.remove(int(li[1]))
    if li[0] == 'append':
        list.append(int(li[1]))
    if li[0] == 'sort':
        list.sort()
    if li[0] == 'pop':
        list.pop()
    if li[0] == 'reverse':
        list.reverse()
      
        