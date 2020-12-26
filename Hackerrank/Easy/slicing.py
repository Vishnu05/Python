
# string slicing 

string = 'abcabcabc'
print(string[4])
# string[4] = 'b'

print(string)

a = string[:4] + 'Z' + string[5:]
print(a)

count = 0
l = list()
s = ''
for i in range(5):
    count += 1
    l.append(count)
    print(l)
  
# correct solution, what does this end do??
for i in range(1, 5):
    print(i, end='')


print(l, s)
