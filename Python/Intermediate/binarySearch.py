

# Binary search

# n = int(input('Enter the size of array or list : '))

# ar = list()

# for i in range(n):
#     ar.append(int(input()))

# print('List of ', n, ' no is', ar)


ele = [1, 5, 6, 17, 5, 3]

# print(ele)

ele.sort()

# print(ele)

sea = int(input('enter the element you want to search : '))

# not sure what kind of serach does it use
# if sea in ele:
#     print('true')
# else:
#     print('false')


def binarySearch(ele, sea):
    print('list elements are ', ele, ' element want to search is', sea)

    l = 0
    r = len(ele) - 1
    print('left value is ', l, 'right value is ', r)

    while l <= r:

        # finding the median
        m = int((l + r) / 2)

        if(ele[m] == sea):
            return m

        #
        if (ele[m] < sea):
            l = m + 1
        else:
            r = m - 1

    return -1


result = binarySearch(ele, sea)

if (result == -1):
    print('Search has ended and not able to find the value ')
else:
    print('I found something interesting ')
