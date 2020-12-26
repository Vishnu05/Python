import textwrap
s = input()
n = int(input())

ss = s

# text wrap is a module in the python which helps to form a paragraph
print(textwrap.fill(ss, 4))


count = 0
while(count < len(s)):
    lists = list()
    for j in range(n):
        # print('inner loop starts')
        if (count < len(s)):
            lists.append(s[count])
            count += 1
        # print('count ', count)

    val = ''
    val = val.join(lists)
    print(val)
    # print('outer loop exits ')


# print('Answer ', s[2])
