
right_shifting = int(input())
left_shifting = int(input())

word = 'abcdef'
reverse = word[::-1]

left, right, lshift, rshift = list(), list(), list(), list()

count = 0
for i in word:
    left.append(word[count])
    right.append(reverse[count])
    count += 1
    lshift.append('')
    rshift.append('')

# shiting on the left
count = 0
for i in word:
    if left_shifting < len(word):
        lshift[count] = word[left_shifting]
        left_shifting += 1
        count += 1

    else:
        left_shifting = 0
        lshift[count] = word[left_shifting]
        count += 1
        left_shifting += 1

# # shifting on the right
count = 0
for i in word:
    if right_shifting < len(word):
        rshift[count] = lshift[right_shifting]
        count += 1
        right_shifting += 1
    else:
        right_shifting = 0
        rshift[count] = lshift[right_shifting]
        count += 1
        right_shifting += 1

print('Actual value :', word)
print('Left shiting : ', lshift)
print('Final value after shiting is done', rshift)
